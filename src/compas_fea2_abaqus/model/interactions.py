from compas_fea2.model.interactions import HardContactFrictionPenalty
from compas_fea2.model.interactions import LinearContactFrictionPenalty
from compas_fea2.model.interactions import HardContactRough
from compas_fea2.model.interactions import SurfaceConvection
from compas_fea2.model.interactions import SurfaceRadiation


class AbaqusHardContactFrictionPenalty(HardContactFrictionPenalty):
    """Abaqus implementation of the :class:`HardContactFrictionPenalty`.\n"""

    __doc__ += HardContactFrictionPenalty.__doc__

    def __init__(self, *, mu, tol=0.005, **kwargs) -> None:
        super(AbaqusHardContactFrictionPenalty, self).__init__(mu=mu, tol=tol, **kwargs)

    def jobdata(self):
        return """*Surface Interaction, name={}
*Friction, slip tol={}
{},
*Surface Behavior, pressure-overclosure={}
**""".format(
            self._name, self._tol, self._tangent, self._normal
        )


class AbaqusLinearContactFrictionPenalty(LinearContactFrictionPenalty):
    """Abaqus implementation of the :class:`LinearContactFrictionPenalty`.\n"""

    __doc__ += LinearContactFrictionPenalty.__doc__

    def __init__(self, *, mu, tol=0.005, **kwargs) -> None:
        super(AbaqusLinearContactFrictionPenalty, self).__init__(mu=mu, tol=tol, **kwargs)

    def _generate_jobdata(self):
        return """*Surface Interaction, name={}
*Friction, slip tol={}
{},
*Surface Behavior, pressure-overclosure={}
{}
**""".format(
            self._name, self._tolerance, self._tangent, self._normal, self._stiffness
        )


class AbaqusHardContactRough(HardContactRough):
    """Abaqus implementation of the :class:`HardContactRough`.\n"""

    __doc__ += HardContactRough.__doc__

    def __init__(self, **kwargs) -> None:
        super(AbaqusHardContactRough, self).__init__(**kwargs)

    def _generate_jobdata(self):
        return """*Surface Interaction, name={}
*Friction, rough
*Surface Behavior, pressure-overclosure={}
**""".format(
            self._name, self._normal
        )


class AbaqusSurfaceConvection(SurfaceConvection):
    """Abaqus implementation of the :class:`HardContactNoFriction`.\n"""

    __doc__ += SurfaceConvection.__doc__

    def __init__(self, surface, h, temperature, **kwargs) -> None:
        super(AbaqusSurfaceConvection, self).__init__(surface=surface, h=h, temperature=temperature, **kwargs)

    def jobdata(self):
        data_interface = []
        data_interface.append(f"** Name: {self.name} Type: Convection interaction")
        data_interface.append("*Sfilm")
        if self.temperature.amplitude:
            data_interface[-1] += f", amplitude={self.temperature.amplitude.name}"
        data_interface.append(f"{self.surface._name}_i, F, {self.temperature.temperature}, {self.h}")
        return "\n".join(data_interface)
        return f"""**Convection Interaction, name={self.name}
*Sfilm
{self.surface.name}_i, F, {self.temperature}, {self.h}
**"""


class AbaqusSurfaceRadiation(SurfaceRadiation):
    """Abaqus implementation of the :class:`HardContactNoFriction`.\n"""

    __doc__ += SurfaceConvection.__doc__

    def __init__(self, surface, eps, temperature, **kwargs) -> None:
        super().__init__(surface=surface, eps=eps, temperature=temperature, **kwargs)

    def jobdata(self):
        data_interface = []
        data_interface.append(f"** Name: {self.name} Type: Radiation interaction")
        data_interface.append("*Sradiate")
        if self.temperature.amplitude:
            data_interface[-1] += f", amplitude={self.temperature.amplitude.name}"
        data_interface.append(f"{self.surface._name}_i, R, {self.temperature.temperature}, {self.eps}")
        return "\n".join(data_interface)
        return f"""**Radiation Interaction, name={self.name}
*Sradiate
{self.surface.name}_i, R, {self.temperature.temperature}, {self.eps}
**"""
