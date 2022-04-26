from neurophotonics.probe.probely import Probe, ProbeGroup


def design1(save=False, output="Design1.csv"):
    # The number & places of the detectors and emitters are the same as in Design1.
    # The only difference is the angle of the side shanks and their distance to the
    # center.

    # Create 3 Probes at 0, 0, 0
    # 360 e-pixels
    P1 = Probe(
        probe_dimensions=[1200, 120, 1300],
        n_e_box=[5, 60],
        e_box_length=10,
        e_box_sep=10,
        e_box_vertical_margin=5,
        e_box_horizontal_margin=15,
        n_d_box=[0, 0],
        d_box_length=0,
        d_box_sep=0,
        d_box_vertical_margin=0,
        d_box_horizontal_margin=0,
        name="P1",
    )

    # 4036 d-pixels
    P2 = Probe(
        probe_dimensions=[1200, 120, 1300],
        n_e_box=[5, 60],
        e_box_length=10,
        e_box_sep=10,
        e_box_vertical_margin=5,
        e_box_horizontal_margin=15,
        n_d_box=[22, 240],
        d_box_length=5,
        d_box_sep=0,
        d_box_vertical_margin=5,
        d_box_horizontal_margin=5,
        name="P2",
    )

    P2.e_pixels = []

    # 360 e-pixels
    P3 = Probe(
        probe_dimensions=[1200, 120, 1300],
        n_e_box=[5, 60],
        e_box_length=10,
        e_box_sep=10,
        e_box_vertical_margin=5,
        e_box_horizontal_margin=15,
        n_d_box=[0, 0],
        d_box_length=0,
        d_box_sep=0,
        d_box_vertical_margin=0,
        d_box_horizontal_margin=0,
        name="P3",
    )

    PG = ProbeGroup([P1, P2, P3])

    # Position the Probes
    PG.probes[0].translate([-150, 0, 0])
    PG.probes[0].rotate_around(["br", "tr"], -75)

    PG.probes[2].translate([150, 0, 0])
    PG.probes[2].rotate_around(["bl", "tl"], 75)

    if save:
        df = PG.to_df()
        df.to_csv(output, index=False)

    return PG


def design2(save=False, output="Design2.csv"):
    # Create 10 probes at 0, 0, 0
    PG = ProbeGroup(
        [
            Probe(
                probe_dimensions=[1200, 150, 1300],
                n_e_box=[5, 60],
                e_box_length=10,
                e_box_sep=10,
                e_box_vertical_margin=5,
                e_box_horizontal_margin=30,
                n_d_box=[22, 240],
                d_box_length=5,
                d_box_sep=0,
                d_box_vertical_margin=0,
                d_box_horizontal_margin=25,
                name="P" + str(i),
            )
            for i in range(10)
        ]
    )

    # Position the Probes
    for i, probe in enumerate(PG.probes):
        if not i % 2:
            probe.rotate("z", 180)  # Around the origin (0, 0, 0)
            probe.translate([-150.0 * len(PG.probes) / 2 + 0.5 + i * 150.0, 75, 0])
        else:
            probe.translate([-150.0 * len(PG.probes) / 2 + 0.5 + i * 150.0, -75, 0])

    if save:
        df = PG.to_df()
        df.to_csv(output, index=False)

    return PG