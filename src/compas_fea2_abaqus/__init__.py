"""
********************************************************************************
compas_fea2_abaqus
********************************************************************************
"""

from __future__ import print_function

__author__ = ["Francesco Ranaudo"]
__copyright__ = "Francesco Ranaudo"
__license__ = "MIT License"
__email__ = "ranaudo@arch.ethz.ch"
__version__ = "0.1.0"

import os

HERE = os.path.dirname(__file__)

HOME = os.path.abspath(os.path.join(HERE, "../../"))
DATA = os.path.abspath(os.path.join(HOME, "data"))
DOCS = os.path.abspath(os.path.join(HOME, "docs"))
TEMP = os.path.abspath(os.path.join(HOME, "temp"))


__all__ = ["HOME", "DATA", "DOCS", "TEMP"]

from pydoc import ErrorDuringImport
import compas_fea2

from compas.plugins import plugin

# Materials
from compas_fea2.model.materials import (
    ElasticIsotropic,
    ElasticOrthotropic,
    ElasticPlastic,
    Stiff,
    UserMaterial,
    Concrete,
    ConcreteDamagedPlasticity,
    ConcreteSmearedCrack,
    Steel,
    Timber,
)

# Boundary Conditions
from compas_fea2.model.bcs import (
    GeneralBC,
    FixedBC,
    ClampBCXX,
    ClampBCYY,
    ClampBCZZ,
    PinnedBC,
    RollerBCX,
    RollerBCXY,
    RollerBCXZ,
    RollerBCY,
    RollerBCYZ,
    RollerBCZ,
)

# Constraints
from compas_fea2.model.constraints import (
    TieMPC,
    BeamMPC,
    TieConstraint,
)

# Intial Conditions
from compas_fea2.model.ics import (
    InitialTemperatureField,
    InitialStressField,
)

# Elements
from compas_fea2.model.elements import (
    MassElement,
    BeamElement,
    TrussElement,
    MembraneElement,
    ShellElement,
    _Element3D,
    TetrahedronElement,
    HexahedronElement,
)

# Groups
from compas_fea2.model.groups import (
    NodesGroup,
    ElementsGroup,
    FacesGroup,
)

# Models
from compas_fea2.model import Model

# Nodes
from compas_fea2.model import Node

# Parts
from compas_fea2.model import DeformablePart, RigidPart

# Releases
from compas_fea2.model.releases import (
    BeamEndPinRelease,
)

# Sections
from compas_fea2.model.sections import (
    AngleSection,
    BeamSection,
    BoxSection,
    CircularSection,
    HexSection,
    ISection,
    MassSection,
    PipeSection,
    RectangularSection,
    SpringSection,
    StrutSection,
    TieSection,
    TrapezoidalSection,
    TrussSection,
    MembraneSection,
    ShellSection,
    SolidSection,
)


# Steps
from compas_fea2.problem.steps import (
    ModalAnalysis,
    ComplexEigenValue,
    StaticStep,
    LinearStaticPerturbation,
    BucklingAnalysis,
    DynamicStep,
    QuasiStaticStep,
    DirectCyclicStep,
)
# Displacements
from compas_fea2.problem.displacements import (
    GeneralDisplacement,
)
# Fields
from compas_fea2.problem.fields import (
    PrescribedTemperatureField,
)
# Loads
from compas_fea2.problem.loads import (
    PointLoad,
    LineLoad,
    AreaLoad,
    TributaryLoad,
    PrestressLoad,
    GravityLoad,
    HarmonicPointLoad,
    HarmonicPressureLoad,
    ThermalLoad
)

# Outputs
from compas_fea2.problem.outputs import (
    FieldOutput,
    HistoryOutput,
)

# Problem
from compas_fea2.problem import Problem

# Results
from compas_fea2.results import (
    Results,
    StepResults,
)

# Input File
from compas_fea2.job import (
    InputFile,
    ParametersFile,
)
# =========================================================================
#                           ABAQUS CLASSES
# =========================================================================

try:
    # Abaqus Models
    from .model import AbaqusModel
    from .model import AbaqusDeformablePart, AbaqusRigidPart
    from .model import AbaqusNode

    # Abaqus Elements
    from .model.elements import (
        AbaqusMassElement,
        AbaqusBeamElement,
        AbaqusTrussElement,
        AbaqusMembraneElement,
        AbaqusShellElement,
        _AbaqusElement3D,
        AbaqusTetrahedronElement,
        AbaqusHexahedronElement,
    )

    # Abaqus Sections
    from .model.sections import (
        AbaqusAngleSection,
        AbaqusBeamSection,
        AbaqusBoxSection,
        AbaqusCircularSection,
        AbaqusHexSection,
        AbaqusISection,
        AbaqusMassSection,
        AbaqusPipeSection,
        AbaqusRectangularSection,
        AbaqusSpringSection,
        AbaqusStrutSection,
        AbaqusTieSection,
        AbaqusTrapezoidalSection,
        AbaqusTrussSection,
        AbaqusMembraneSection,
        AbaqusShellSection,
        AbaqusSolidSection,
    )

    # Abaqus Materials
    from .model.materials import (
        AbaqusElasticIsotropic,
        AbaqusElasticOrthotropic,
        AbaqusElasticPlastic,
        AbaqusStiff,
        AbaqusUserMaterial,
        AbaqusConcrete,
        AbaqusConcreteDamagedPlasticity,
        AbaqusConcreteSmearedCrack,
        AbaqusSteel,
        AbaqusTimber,
    )

    # Abaqus Groups
    from .model.groups import (
        AbaqusNodesGroup,
        AbaqusElementsGroup,
        AbaqusFacesGroup,
    )

    # Abaqus Constraints
    from .model.constraints import (
        AbaqusTieMPC,
        AbaqusBeamMPC,
        AbaqusTieConstraint,
    )

    # Abaqus Initial Conditions
    from .model.ics import (
        AbaqusInitialTemperatureField,
        AbaqusInitialStressField,
    )

    # Abaqus release
    from .model.releases import (
        AbaqusBeamEndPinRelease,
    )

    # Abaqus Boundary Conditions
    from .model.bcs import (
        AbaqusGeneralBC,
        AbaqusFixedBC,
        AbaqusFixedBCXX,
        AbaqusFixedBCYY,
        AbaqusFixedBCZZ,
        AbaqusPinnedBC,
        AbaqusRollerBCX,
        AbaqusRollerBCXY,
        AbaqusRollerBCXZ,
        AbaqusRollerBCY,
        AbaqusRollerBCYZ,
        AbaqusRollerBCZ,
    )

    # Abaqus Problem
    from .problem import AbaqusProblem

    # Abaqus Steps
    from .problem.steps import (
        AbaqusModalAnalysis,
        AbaqusComplexEigenValue,
        AbaqusStaticStep,
        AbaqusLinearStaticPerturbation,
        AbaqusBucklingAnalysis,
        AbaqusDynamicStep,
        AbaqusQuasiStaticStep,
        AbaqusDirectCyclicStep,
    )
    # Abaqus Loads
    from .problem.loads import (
        AbaqusPointLoad,
        AbaqusLineLoad,
        AbaqusAreaLoad,
        AbaqusTributaryLoad,
        AbaqusPrestressLoad,
        AbaqusGravityLoad,
        AbaqusHarmonicPointLoad,
        AbaqusHarmonicPressureLoad,
        AbaqusThermalLoad,
    )

    # Abaqus Fields
    from .problem.fields import (
        AbaqusPrescribedTemperatureField,
    )

    # Abaqus Displacements
    from .problem.displacements import (
        AbaqusGeneralDisplacement,
    )

    # Abaqus outputs
    from .problem.outputs import (
        AbaqusFieldOutput,
        AbaqusHistoryOutput,
    )

    # Abaqus Results
    from .results import (
        AbaqusResults,
        AbaqusStepResults,
    )

    # Abaqus Input File
    from .job import(
        AbaqusInputFile,
        AbaqusParametersFile,
    )

    # build the plugin registry
    def register_backend():
        backend = compas_fea2.BACKENDS['compas_fea2_abaqus']


        backend[Model] = AbaqusModel

        backend[DeformablePart] = AbaqusDeformablePart
        backend[RigidPart] = AbaqusRigidPart

        backend[Node] = AbaqusNode

        backend[MassElement] = AbaqusMassElement
        backend[BeamElement] = AbaqusBeamElement
        backend[TrussElement] = AbaqusTrussElement
        backend[MembraneElement] = AbaqusMembraneElement
        backend[ShellElement] = AbaqusShellElement
        backend[_Element3D] = _AbaqusElement3D
        backend[TetrahedronElement] = AbaqusTetrahedronElement
        backend[HexahedronElement] = AbaqusHexahedronElement

        backend[AngleSection] = AbaqusAngleSection
        backend[BeamSection] = AbaqusBeamSection
        backend[BoxSection] = AbaqusBoxSection
        backend[CircularSection] = AbaqusCircularSection
        backend[HexSection] = AbaqusHexSection
        backend[ISection] = AbaqusISection
        backend[MassSection] = AbaqusMassSection
        backend[MembraneSection] = AbaqusMembraneSection
        backend[PipeSection] = AbaqusPipeSection
        backend[RectangularSection] = AbaqusRectangularSection
        backend[ShellSection] = AbaqusShellSection
        backend[SolidSection] = AbaqusSolidSection
        backend[SpringSection] = AbaqusSpringSection
        backend[StrutSection] = AbaqusStrutSection
        backend[TieSection] = AbaqusTieSection
        backend[TrapezoidalSection] = AbaqusTrapezoidalSection
        backend[TrussSection] = AbaqusTrussSection

        backend[ElasticIsotropic] = AbaqusElasticIsotropic
        backend[ElasticOrthotropic] = AbaqusElasticOrthotropic
        backend[ElasticPlastic] = AbaqusElasticPlastic
        backend[Stiff] = AbaqusStiff
        backend[UserMaterial] = AbaqusUserMaterial
        backend[Concrete] = AbaqusConcrete
        backend[ConcreteDamagedPlasticity] = AbaqusConcreteDamagedPlasticity
        backend[ConcreteSmearedCrack] = AbaqusConcreteSmearedCrack
        backend[Steel] = AbaqusSteel
        backend[Timber] = AbaqusTimber

        backend[NodesGroup] = AbaqusNodesGroup
        backend[ElementsGroup] = AbaqusElementsGroup
        backend[FacesGroup] = AbaqusFacesGroup

        backend[TieMPC] = AbaqusTieMPC
        backend[BeamMPC] = AbaqusBeamMPC
        backend[TieConstraint] = AbaqusTieConstraint

        backend[BeamEndPinRelease] = AbaqusBeamEndPinRelease

        backend[InitialTemperatureField] = AbaqusInitialTemperatureField
        backend[InitialStressField] = AbaqusInitialStressField

        backend[GeneralBC] = AbaqusGeneralBC
        backend[FixedBC] = AbaqusFixedBC
        backend[ClampBCXX] = AbaqusFixedBCXX
        backend[ClampBCYY] = AbaqusFixedBCYY
        backend[ClampBCZZ] = AbaqusFixedBCZZ
        backend[PinnedBC] = AbaqusPinnedBC
        backend[RollerBCX] = AbaqusRollerBCX
        backend[RollerBCXY] = AbaqusRollerBCXY
        backend[RollerBCXZ] = AbaqusRollerBCXZ
        backend[RollerBCY] = AbaqusRollerBCY
        backend[RollerBCYZ] = AbaqusRollerBCYZ
        backend[RollerBCZ] = AbaqusRollerBCZ

        backend[Problem] = AbaqusProblem

        backend[ModalAnalysis] = AbaqusModalAnalysis
        backend[ComplexEigenValue, StaticStep] = AbaqusComplexEigenValue
        backend[StaticStep] = AbaqusStaticStep
        backend[LinearStaticPerturbation] = AbaqusLinearStaticPerturbation
        backend[BucklingAnalysis] = AbaqusBucklingAnalysis
        backend[DynamicStep] = AbaqusDynamicStep
        backend[QuasiStaticStep] = AbaqusQuasiStaticStep
        backend[DirectCyclicStep] = AbaqusDirectCyclicStep

        backend[GravityLoad] = AbaqusGravityLoad
        backend[PointLoad] = AbaqusPointLoad
        backend[LineLoad] = AbaqusLineLoad
        backend[AreaLoad] = AbaqusAreaLoad
        backend[TributaryLoad] = AbaqusTributaryLoad
        backend[PrestressLoad] = AbaqusPrestressLoad
        backend[HarmonicPointLoad] = AbaqusHarmonicPointLoad
        backend[HarmonicPressureLoad] = AbaqusHarmonicPressureLoad
        backend[ThermalLoad] = AbaqusThermalLoad

        backend[GeneralDisplacement] = AbaqusGeneralDisplacement

        backend[PrescribedTemperatureField] = AbaqusPrescribedTemperatureField

        backend[FieldOutput] = AbaqusFieldOutput
        backend[HistoryOutput] = AbaqusHistoryOutput

        backend[Results] = AbaqusResults
        backend[StepResults] = AbaqusStepResults

        backend[InputFile] = AbaqusInputFile
        backend[ParametersFile] = AbaqusParametersFile

        print('Abaqus implementations registered...')
except:
    raise ErrorDuringImport()
