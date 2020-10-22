import cadquery as cq

from paramak import RotateMixedShape


class RotateStraightShape(RotateMixedShape):
    """Rotates a 3d CadQuery solid from points connected with straight
    connections.

    Args:
        points (list): list of (float, float) containing each point
            coordinates.
        rotation_angle (float): The rotation angle to use when revolving the
            solid (degrees).
        stp_filename (str, optional): Defaults to "RotateStraightShape.stp".
        stl_filename (str, optional): Defaults to "RotateStraightShape.stl".
    """

    def __init__(
        self,
        rotation_angle=360.0,
        stp_filename="RotateStraightShape.stp",
        stl_filename="RotateStraightShape.stl",
        **kwargs
    ):

        super().__init__(
            rotation_angle=rotation_angle,
            stp_filename=stp_filename,
            stl_filename=stl_filename,
            **kwargs
        )

    def add_connections(self, points):
        if points is not None:
            return [(*p, "straight") for p in points]
