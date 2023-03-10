from dash import dcc

num_models_slider = dcc.Slider(
                            id='nm',
                            min=1, max=5, step=1,
                            marks={0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5'},
                            value=2,
                        )

num_points_slider = dcc.Slider(
                                id='n',
                                min=100, max=1000, step=100,
                                marks={100: '100',
                                       200: '200',
                                       300: '300',
                                       400: '400',
                                       500: '500',
                                       600: '600',
                                       700: '700',
                                       800: '800',
                                       900: '900',
                                       1000: '1000'},
                                value=500
                            )

noise_perc_slider = dcc.Slider(
                                id='noise_perc',
                                min=0, max=0.1, step=0.01,
                                marks={0: '0.0',
                                       0.01: '0.01',
                                       0.02: '0.02',
                                       0.03: '0.03',
                                       0.04: '0.04',
                                       0.05: '0.05',
                                       0.06: '0.06',
                                       0.07: '0.07',
                                       0.08: '0.08',
                                       0.09: '0.09',
                                       0.1: '0.10'},
                                value=0.01
                            )

outliers_perc_slider = dcc.Slider(
                                id='outliers_perc',
                                min=0, max=1, step=0.10,
                                marks={0: '0.0',
                                       0.1: '0.1',
                                       0.2: '0.2',
                                       0.3: '0.3',
                                       0.4: '0.4',
                                       0.5: '0.5',
                                       0.6: '0.6',
                                       0.7: '0.7',
                                       0.8: '0.8',
                                       0.9: '0.9',
                                       1: '1.0'},
                                value=0.1
                            )

radii_range_slider =  dcc.RangeSlider(
                                        id='radius',
                                        min=0.1, max=1.0, step=0.10,
                                        marks={0: '0.0',
                                               0.1: '0.1',
                                               0.2: '0.2',
                                               0.3: '0.3',
                                               0.4: '0.4',
                                               0.5: '0.5',
                                               0.6: '0.6',
                                               0.7: '0.7',
                                               0.8: '0.8',
                                               0.9: '0.9',
                                               1: '1.0'},
                                        value=[0.3, 0.5]
                                    )