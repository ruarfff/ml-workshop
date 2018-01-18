# Distributed MapReduce with TensorFlow

One way to see this working:

Open 4 terminal windows. Make sure to enter the vitrualen for TensorFlow we setup before.

Then in each terminal, load one configuration and run count.py

For example:

#### Terminal 1
```bash
source config_files_0.sh
python count.py
```

#### Terminal 2
```bash
source config_map_0.sh
python count.py
```

#### Terminal 3
```bash
source config_map_1.sh
python count.py
```

#### Terminal 4
```bash
source config_reduce_0.sh
python count.py
```