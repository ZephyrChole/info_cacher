import pickle
import os
import glob
from datetime import date


class InfoCacher:
    def __init__(self, dir_, name):
        self.dir_ = dir_
        self.name = name
        self.history_file_path = os.path.join(self.dir_, self.get_history_filename(self.name))

    def get_history_filename(self, name):
        return '{}_history_{}.pickle'.format(name, self.get_today_str())

    def get_today_str(self):
        today = date.today()
        return '{}{}{}'.format(str(today.year).rjust(2, '0'), str(today.month).rjust(2, '0'),
                               str(today.day).rjust(2, '0'))

    @property
    def has_valid_cache(self):
        return os.path.exists(self.history_file_path) and os.path.isfile(self.history_file_path)

    def loads(self):
        with open(self.history_file_path, 'rb') as file:
            return pickle.loads(file.read())

    def dumps(self, something):
        self.clear_old()
        with open(self.history_file_path, 'wb') as file:
            file.write(pickle.dumps(something))

    def clear_old(self):
        for f in glob.glob(os.path.join(self.dir_, f'{self.name}_history_*.pickle')):
            os.remove(f)
