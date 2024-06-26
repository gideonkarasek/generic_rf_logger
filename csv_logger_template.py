import logging
from csv_logger import CsvLogger
from datetime import date


def log_results(freq, chan_1, chan_2, diff, phase, count, test_name):
    filename = f'Logs/{test_name} Test Log {date.today().strftime("%Y%m%d")}.csv'
    fmt = '%(asctime)s,%(message)s'
    datefmt = '%Y%m%d %H:%M:%S'
    level = logging.INFO
    header = ['frequency', 'fwd_power', 'ref_power', 'return_loss', 'phase', 'count']
    mhz = float(freq) / 1000000
    chan_1 = float(chan_1)
    chan_2 = float(chan_2)
    diff = float(diff)
    phase = float(phase)
    count = int(count)

    logger = CsvLogger(filename=filename,
                       fmt=fmt,
                       datefmt=datefmt,
                       level=level,
                       header=header)

    logger.info([float(mhz), float(chan_1), float(chan_2), float(diff), float(phase), int(count)])


def log_results_sweep(count, freq, current_power, target_power, sweep_step):
    filename = 'log_sweep_sim1.csv'
    fmt = '%(asctime)s,%(message)s'
    datefmt = '%m/%d %H:%M:%S'
    level = logging.INFO
    header = ['date', 'count', 'frequency', 'current power', 'target power', 'step size']
    mhz = float(freq) / 1000000

    logger = CsvLogger(filename=filename,
                       fmt=fmt,
                       datefmt=datefmt,
                       level=level,
                       header=header)

    logger.info([float(count), float(mhz), float(current_power), float(target_power), float(sweep_step)])
