# Adds this config as an environment variable that TensorFlow understands
export TF_CONFIG='{
  "cluster": {
    "files": [
      "localhost:2222"
    ], 
    "map": [
      "localhost:2224", 
      "localhost:2225"
    ], 
    "reduce": [
      "localhost:2223"
    ]
  }, 
  "task": {
    "index": 1, 
    "type": "map"
  }
}'
# Here we are telling TensorFlow not to use our GPU
export CUDA_VISIBLE_DEVICES=-1
