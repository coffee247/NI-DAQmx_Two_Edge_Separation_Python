import nidaqmx

with nidaqmx.Task() as task:
    task.ci_channels.add_ci_two_edge_sep_chan("Dev1/ctr0", min_val=0.0000001,
                                                max_val=1.0, units=nidaqmx.constants.TimeUnits.SECONDS,
                                                first_edge=nidaqmx.constants.Edge.RISING,
                                                second_edge=nidaqmx.constants.Edge.FALLING)


    print('\nPerforming sample read .... This will \"Time out\" after 10 seconds if no data recieved: ')

    data = 0.0
    data = task.read()
    print(data)
