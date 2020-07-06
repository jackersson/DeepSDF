
### Fetch data
```
# Downloaded data placed to data/ShapeNetV2/plane

# Visualize
python visualize_mesh.py -f data/ShapeNetV2/plane/24_simplified.obj
```


### Preprocess
```
# SDF values (Train)
python preprocess_data.py --data_dir data/processed --source data/ShapeNetV2/ --name ShapeNetV2 --split examples/splits/ShapeNetV2_planes_small_train.json --test --skip

# Surface (Test)
python preprocess_data.py --data_dir data/processed --source data/ShapeNetV2/ --name ShapeNetV2 --split examples/splits/ShapeNetV2_planes_tiny_test.json --surface --skip
```

### Train
```
python train_deep_sdf.py -e examples/planes/ -c latest

python plot_log.py -e examples/planes
```

### Reconstruct
```
python reconstruct.py -e examples/planes -c 100 --split examples/splits/ShapeNetV2_planes_tiny_test.json -d data/processed --skip
```

- **Visualize**

```
python visualize_mesh.py -f examples/planes/Reconstructions/100/Meshes/ShapeNetV2/plane/24_simplified.ply
```

### Eval
```
python evaluate.py -e examples/planes/ -c 100 --split examples/splits/ShapeNetV2_planes_tiny_test.json -d data/processed
```

```
shape, chamfer_dist
ShapeNetV2/plane/3123_simplified, 0.0017568532187549493
ShapeNetV2/plane/2240_simplified, 0.00014260457348149895
ShapeNetV2/plane/2625_simplified, 0.00017248503760398855
ShapeNetV2/plane/2494_simplified, 0.0001840932501527067
ShapeNetV2/plane/662_simplified, 0.00203074206434161
ShapeNetV2/plane/2215_simplified, 0.0001446743141816077
ShapeNetV2/plane/3506_simplified, 0.00037945155898906467
ShapeNetV2/plane/1706_simplified, 0.0004534628688223154
ShapeNetV2/plane/3397_simplified, 0.000304452812999803
ShapeNetV2/plane/1946_simplified, 0.0011356243426132852
ShapeNetV2/plane/2655_simplified, 0.0007481785957675503
ShapeNetV2/plane/3891_simplified, 0.0010259146670111028
ShapeNetV2/plane/3529_simplified, 0.012941905042290772
ShapeNetV2/plane/3872_simplified, 0.0014115441453774857
ShapeNetV2/plane/2285_simplified, 0.00022235365195158148
ShapeNetV2/plane/3585_simplified, 0.0003327252260218053
ShapeNetV2/plane/1443_simplified, 0.0005372506960316105
ShapeNetV2/plane/1095_simplified, 0.0006375614609531874
ShapeNetV2/plane/931_simplified, 0.00023509833208038234
ShapeNetV2/plane/2654_simplified, 0.00023513590402602025
ShapeNetV2/plane/2682_simplified, 0.0002578531399455278
```