from compas_fea2.problem.fields import ForceField
from compas_fea2.problem.fields import GravityLoadField
from compas_fea2.problem.fields import TemperatureField
from compas_fea2.problem.fields import DisplacementField

from compas_fea2.units import no_units, m, s


dofs = ["x", "y", "z", "xx", "yy", "zz"]


class AbaqusTemperatureField(TemperatureField):
    """Calculix implementation of :class:`PrescribedTemperatureField`.\n"""

    __doc__ = (__doc__ or "") + (TemperatureField.__doc__ or "")

    def __init__(self, temperature, distribution, load_case, combination_rank=1, **kwargs):
        super().__init__(
            temperature,
            distribution,
            load_case,
            combination_rank=combination_rank,
            **kwargs,
        )

    @property
    @no_units
    def jobdata(self):
        """Generates the string information for the input file.

        Parameters
        ----------
        None

        Returns
        -------
        input file data line (str).

        """
        raise NotImplementedError("Abaqus TemperatureField jobdata not implemented yet.")


class AbaqusForceField(ForceField):
    """Calculix implementation of :class:`ForceField`.\n"""

    __doc__ = (__doc__ or "") + (ForceField.__doc__ or "")

    def __init__(
        self,
        loads,
        distribution,
        load_case=None,
        combination_rank=1,
        modify=False,
        follow=False,
        **kwargs,
    ):
        super().__init__(
            loads=loads,
            distribution=distribution,
            load_case=load_case,
            combination_rank=combination_rank,
            **kwargs,
        )
        self._modify = ", OP={}".format(modify) if modify else ", OP=MOD"  # In abaqus the default is MOD
        self._follow = ", follower" if follow else ""

    @property
    @no_units
    def jobdata(self):
        """Generates the string information for the input file.

        Parameters
        ----------
        None

        Returns
        -------
        input file data line (str).
        """
        data_section = [
            "** Name: {} Type: Concentrated Force".format(self.name),
            "*Cload{}{}".format(self._modify, self._follow),
        ]

        for node, load in self.node_load:
            for comp, dof in enumerate(dofs, 1):
                if getattr(load, dof):
                    data_section.append(f"{node.part.name}-1.{node.key}, {comp}, {getattr(load, dof)}")
        return "\n".join(data_section) or "**"

        # class AbaqusPrescribedTemperatureField(PrescribedTemperatureField):
        #     """Abaqus implementation of :class:`PrescribedTemperatureField`.\n"""

        data_section = [
            "** Name: {} Type: Concentrated Force".format(self.name),
            "*Cload{}{}".format(self._modify, self._follow),
        ]

        for node, load in self.node_load:
            for comp, dof in enumerate(dofs, 1):
                if getattr(load, dof):
                    data_section.append(f"{node.part.name}-1.{node.key}, {comp}, {getattr(load, dof)}")
        return "\n".join(data_section) or "**"


class AbaqusGravityLoadField(GravityLoadField):
    """Calculix implementation of :class:`GravityLoadField`.\n"""

    __doc__ = (__doc__ or "") + (GravityLoadField.__doc__ or "")

    def __init__(
        self,
        g=9.81 * m / s**2,
        direction=(0, 0, -1),
        distribution=None,
        load_case=None,
        combination_rank=1,
        **kwargs,
    ):
        super().__init__(
            g=g,
            direction=direction,
            distribution=distribution,
            load_case=load_case,
            combination_rank=combination_rank,
            **kwargs,
        )

    @property
    @no_units
    def jobdata(self):
        """Generates the string information for the input file.

        Parameters
        ----------
        None

        Returns
        -------
        input file data line (str).
        """
        return (
            f"** Name: {self.name} Type: Gravity\n"
            "*Dload\n"
            f", GRAV, {self.g}, {self.direction[0]}, {self.direction[1]}, {self.direction[2]}"
        )


class AbaqusDisplacementField(DisplacementField):
    def __init__(
        self,
        displacements,
        distribution,
        modify=False,
        follow=False,
        load_case=None,
        combination_rank=1,
        **kwargs,
    ):
        super().__init__(displacements, distribution, load_case, combination_rank, **kwargs)
        self._modify = ", OP={}".format(modify) if modify else ", OP=MOD"  # In abaqus the default is MOD
        self._follow = ", follower" if follow else ""

    @property
    def jobdata(self):
        # Boundary conditions is updated to remove BC on nodes with imposed displacement
        data_section = [
            "** Name: {} Type: Boundary Condition".format(self.name),
            "*Boundary{}{}".format(self._modify, self._follow),
        ]

        for bc, nodes in self.model.bcs_nodes.items():
            for node in nodes:
                for comp, dof in enumerate(dofs, 1):
                    if getattr(bc, dof) and node not in self.distribution:
                        data_section.append(f"{node.part.name}-1.{node.key}, {comp}")
        data_section.append(f"** Name: {self.name} Type:  Displacement/Rotation".format())
        data_section.append("*Boundary, OP=MOD")

        for node, displacement in self.node_displacement:
            for comp, dof in enumerate(dofs, 1):
                if getattr(displacement, dof):
                    data_section.append(f"{node.part.name}-1.{node.key}, {comp}, {comp}, {getattr(displacement, dof)}")
        return "\n".join(data_section)
