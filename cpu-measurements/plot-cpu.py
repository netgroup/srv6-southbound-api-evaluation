from __future__ import (unicode_literals, division, print_function, absolute_import)

import time,psutil


def monitor(logfile=None, plot=None, duration=None, samplingInterval=None):

    # Record start time
    start_time = time.time()

    if logfile:
        f = open(logfile, 'w')
        f.write("# {0:12s} {1:12s}\n".format(
            'Elapsed time'.center(12),
            'CPU (%)'.center(12),)
        )

    log = {}
    log['times'] = []
    log['cpu'] = []

    psutil.cpu_percent(interval=None, percpu=False)

    try:

        # Start main event loop
        while True:

            # Find current time
            current_time = time.time()

            # Check if we have reached the maximum time
            if duration is not None and current_time - start_time > duration:
                break

            # Get current CPU and memory
            try:
                current_cpu = psutil.cpu_percent(interval=None, percpu=False)
            except Exception:
                break

            if logfile:
                f.write("{0:12.3f} {1:12.3f}\n".format(
                    current_time - start_time,
                    current_cpu))
                f.flush()

            if samplingInterval is not None:
                time.sleep(samplingInterval)

            # If plotting, record the values
            if plot:
                log['times'].append(current_time - start_time)
                log['cpu'].append(current_cpu)

    except KeyboardInterrupt:  # pragma: no cover
        pass

    if logfile:
        f.close()

    if plot:

        import matplotlib.pyplot as plt

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        ax.plot(log['times'], log['cpu'], '-', lw=1, color='r')

        ax.set_ylabel('CPU (%)', color='r')
        ax.set_xlabel('time (s)')
        ax.set_ylim(0., max(log['cpu']) * 1.2)

        ax.grid()

        fig.savefig(plot)


if __name__ == '__main__':
    monitor(logfile="logfile.txt", plot="plot.png", duration=None, samplingInterval=0.1)