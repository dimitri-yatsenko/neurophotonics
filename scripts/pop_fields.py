from neurophotonics.fields import *

try:
    EField.populate(reserve_jobs=True, processes=1024, display_progress=False)
except ValueError:
    print("Efield already populated")

try:
    DField.populate(reserve_jobs=True, processes=1024, display_progress=False)
except ValueError:
    print("Dfield already populated")