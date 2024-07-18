C:.
│   .dvcignore
│   .gitignore
│   project_structure.md
│   README.md
│
├───.dvc
│   │   .gitignore
│   │   config
│   │
│   ├───cache
│   │   └───files
│   │       └───md5
│   │           ├───02
│   │           │       a2ad182d082d90819470072c76121c
│   │           │
│   │           ├───04
│   │           │       fb1368375e982da57fd49e8c7e7ba9
│   │           │
│   │           ├───06
│   │           │       7f892ff7bde3f72a4610fc0a8a81b2
│   │           │
│   │           ├───1f
│   │           │       1220d64fba46047579be951d610b8d
│   │           │
│   │           ├───56
│   │           │       96e61638ac9aab0773b7758503554c
│   │           │
│   │           └───8c
│   │                   0204761d930fc9188725688a79f9e3
│   │
│   └───tmp
│           btime
│           lock
│           rwlock
│           rwlock.lock
│
├───catboost_info
│   │   catboost_training.json
│   │   learn_error.tsv
│   │   time_left.tsv
│   │
│   ├───learn
│   │       events.out.tfevents
│   │
│   └───tmp
├───csv
│   ├───apartments
│   │       apartments_pl_2023_08.csv
│   │       apartments_pl_2023_09.csv
│   │       apartments_pl_2023_10.csv
│   │       apartments_pl_2023_11.csv
│   │       apartments_pl_2023_12.csv
│   │       apartments_pl_2024_01.csv
│   │       apartments_pl_2024_02.csv
│   │       apartments_pl_2024_03.csv
│   │       apartments_pl_2024_04.csv
│   │       apartments_pl_2024_05.csv
│   │       apartments_pl_2024_06.csv
│   │
│   └───rent
│           apartments_rent_pl_2023_11.csv
│           apartments_rent_pl_2023_12.csv
│           apartments_rent_pl_2024_01.csv
│           apartments_rent_pl_2024_02.csv
│           apartments_rent_pl_2024_03.csv
│           apartments_rent_pl_2024_04.csv
│           apartments_rent_pl_2024_05.csv
│           apartments_rent_pl_2024_06.csv
│
├───data
│   ├───processed
│   │   ├───housing
│   │   │       .gitignore
│   │   │       test_housing.csv
│   │   │       test_housing.csv.dvc
│   │   │       train_housing.csv
│   │   │       train_housing.csv.dvc
│   │   │
│   │   └───rent
│   │           .gitignore
│   │           test_rent.csv
│   │           test_rent.csv.dvc
│   │           train_rent.csv
│   │           train_rent.csv.dvc
│   │
│   └───raw
│       ├───housing
│       │       .gitignore
│       │       apartments.csv
│       │       apartments.csv.dvc
│       │
│       └───rent
│               .gitignore
│               rent.csv
│               rent.csv.dvc
│
├───mlruns
│   ├───.trash
│   ├───0
│   │       meta.yaml
│   │
│   ├───468286246391009035
│   │   │   meta.yaml
│   │   │
│   │   ├───090c7f32a63547db9dd5a78c21cef401
│   │   │   │   meta.yaml
│   │   │   │
│   │   │   ├───artifacts
│   │   │   │   └───xgboost_rent
│   │   │   │           conda.yaml
│   │   │   │           MLmodel
│   │   │   │           model.pkl
│   │   │   │           python_env.yaml
│   │   │   │           requirements.txt
│   │   │   │
│   │   │   ├───metrics
│   │   │   │       train_r2
│   │   │   │       val_mse
│   │   │   │       val_r2
│   │   │   │
│   │   │   ├───params
│   │   │   │       base_score
│   │   │   │       booster
│   │   │   │       callbacks
│   │   │   │       colsample_bylevel
│   │   │   │       colsample_bynode
│   │   │   │       colsample_bytree
│   │   │   │       device
│   │   │   │       early_stopping_rounds
│   │   │   │       enable_categorical
│   │   │   │       eval_metric
│   │   │   │       feature_types
│   │   │   │       gamma
│   │   │   │       grow_policy
│   │   │   │       importance_type
│   │   │   │       interaction_constraints
│   │   │   │       learning_rate
│   │   │   │       max_bin
│   │   │   │       max_cat_threshold
│   │   │   │       max_cat_to_onehot
│   │   │   │       max_delta_step
│   │   │   │       max_depth
│   │   │   │       max_leaves
│   │   │   │       min_child_weight
│   │   │   │       missing
│   │   │   │       monotone_constraints
│   │   │   │       multi_strategy
│   │   │   │       num_parallel_tree
│   │   │   │       n_estimators
│   │   │   │       n_jobs
│   │   │   │       objective
│   │   │   │       random_state
│   │   │   │       reg_alpha
│   │   │   │       reg_lambda
│   │   │   │       sampling_method
│   │   │   │       scale_pos_weight
│   │   │   │       subsample
│   │   │   │       tree_method
│   │   │   │       validate_parameters
│   │   │   │       verbosity
│   │   │   │
│   │   │   └───tags
│   │   │           mlflow.log-model.history
│   │   │           mlflow.runName
│   │   │           mlflow.source.git.commit
│   │   │           mlflow.source.name
│   │   │           mlflow.source.type
│   │   │           mlflow.user
│   │   │
│   │   ├───26c4065204854c81bf8a3295429e1955
│   │   │   │   meta.yaml
│   │   │   │
│   │   │   ├───artifacts
│   │   │   │   └───lightgbm_rent
│   │   │   │           conda.yaml
│   │   │   │           MLmodel
│   │   │   │           model.pkl
│   │   │   │           python_env.yaml
│   │   │   │           requirements.txt
│   │   │   │
│   │   │   ├───metrics
│   │   │   │       train_r2
│   │   │   │       val_mse
│   │   │   │       val_r2
│   │   │   │
│   │   │   ├───params
│   │   │   │       boosting_type
│   │   │   │       class_weight
│   │   │   │       colsample_bytree
│   │   │   │       importance_type
│   │   │   │       learning_rate
│   │   │   │       max_depth
│   │   │   │       min_child_samples
│   │   │   │       min_child_weight
│   │   │   │       min_split_gain
│   │   │   │       num_leaves
│   │   │   │       n_estimators
│   │   │   │       n_jobs
│   │   │   │       objective
│   │   │   │       random_state
│   │   │   │       reg_alpha
│   │   │   │       reg_lambda
│   │   │   │       subsample
│   │   │   │       subsample_for_bin
│   │   │   │       subsample_freq
│   │   │   │
│   │   │   └───tags
│   │   │           mlflow.log-model.history
│   │   │           mlflow.runName
│   │   │           mlflow.source.git.commit
│   │   │           mlflow.source.name
│   │   │           mlflow.source.type
│   │   │           mlflow.user
│   │   │
│   │   ├───b0af159be639458e96ea3fbc8324bffb
│   │   │   │   meta.yaml
│   │   │   │
│   │   │   ├───artifacts
│   │   │   │   └───random_forest_rent
│   │   │   │           conda.yaml
│   │   │   │           MLmodel
│   │   │   │           model.pkl
│   │   │   │           python_env.yaml
│   │   │   │           requirements.txt
│   │   │   │
│   │   │   ├───metrics
│   │   │   │       train_r2
│   │   │   │       val_mse
│   │   │   │       val_r2
│   │   │   │
│   │   │   ├───params
│   │   │   │       bootstrap
│   │   │   │       ccp_alpha
│   │   │   │       criterion
│   │   │   │       max_depth
│   │   │   │       max_features
│   │   │   │       max_leaf_nodes
│   │   │   │       max_samples
│   │   │   │       min_impurity_decrease
│   │   │   │       min_samples_leaf
│   │   │   │       min_samples_split
│   │   │   │       min_weight_fraction_leaf
│   │   │   │       n_estimators
│   │   │   │       n_jobs
│   │   │   │       oob_score
│   │   │   │       random_state
│   │   │   │       verbose
│   │   │   │       warm_start
│   │   │   │
│   │   │   └───tags
│   │   │           mlflow.log-model.history
│   │   │           mlflow.runName
│   │   │           mlflow.source.git.commit
│   │   │           mlflow.source.name
│   │   │           mlflow.source.type
│   │   │           mlflow.user
│   │   │
│   │   └───e05cb154619145c79f9474fb3dcc19fb
│   │       │   meta.yaml
│   │       │
│   │       ├───artifacts
│   │       │   └───catboost_rent
│   │       │           conda.yaml
│   │       │           MLmodel
│   │       │           model.pkl
│   │       │           python_env.yaml
│   │       │           requirements.txt
│   │       │
│   │       ├───metrics
│   │       │       train_r2
│   │       │       val_mse
│   │       │       val_r2
│   │       │
│   │       ├───params
│   │       │       loss_function
│   │       │       verbose
│   │       │
│   │       └───tags
│   │               mlflow.log-model.history
│   │               mlflow.runName
│   │               mlflow.source.git.commit
│   │               mlflow.source.name
│   │               mlflow.source.type
│   │               mlflow.user
│   │
│   ├───865012712641102509
│   │   │   meta.yaml
│   │   │
│   │   ├───2156c2d9496f4900bdf99feae8a03cd7
│   │   │   │   meta.yaml
│   │   │   │
│   │   │   ├───artifacts
│   │   │   │   └───lightgbm_apartments
│   │   │   │           conda.yaml
│   │   │   │           MLmodel
│   │   │   │           model.pkl
│   │   │   │           python_env.yaml
│   │   │   │           requirements.txt
│   │   │   │
│   │   │   ├───metrics
│   │   │   │       train_r2
│   │   │   │       val_mse
│   │   │   │       val_r2
│   │   │   │
│   │   │   ├───params
│   │   │   │       boosting_type
│   │   │   │       class_weight
│   │   │   │       colsample_bytree
│   │   │   │       importance_type
│   │   │   │       learning_rate
│   │   │   │       max_depth
│   │   │   │       min_child_samples
│   │   │   │       min_child_weight
│   │   │   │       min_split_gain
│   │   │   │       num_leaves
│   │   │   │       n_estimators
│   │   │   │       n_jobs
│   │   │   │       objective
│   │   │   │       random_state
│   │   │   │       reg_alpha
│   │   │   │       reg_lambda
│   │   │   │       subsample
│   │   │   │       subsample_for_bin
│   │   │   │       subsample_freq
│   │   │   │
│   │   │   └───tags
│   │   │           mlflow.log-model.history
│   │   │           mlflow.runName
│   │   │           mlflow.source.git.commit
│   │   │           mlflow.source.name
│   │   │           mlflow.source.type
│   │   │           mlflow.user
│   │   │
│   │   ├───36a088b1c0424c0baf7b249a92dba6f4
│   │   │   │   meta.yaml
│   │   │   │
│   │   │   ├───artifacts
│   │   │   │   └───xgboost_apartments
│   │   │   │           conda.yaml
│   │   │   │           MLmodel
│   │   │   │           model.pkl
│   │   │   │           python_env.yaml
│   │   │   │           requirements.txt
│   │   │   │
│   │   │   ├───metrics
│   │   │   │       train_r2
│   │   │   │       val_mse
│   │   │   │       val_r2
│   │   │   │
│   │   │   ├───params
│   │   │   │       base_score
│   │   │   │       booster
│   │   │   │       callbacks
│   │   │   │       colsample_bylevel
│   │   │   │       colsample_bynode
│   │   │   │       colsample_bytree
│   │   │   │       device
│   │   │   │       early_stopping_rounds
│   │   │   │       enable_categorical
│   │   │   │       eval_metric
│   │   │   │       feature_types
│   │   │   │       gamma
│   │   │   │       grow_policy
│   │   │   │       importance_type
│   │   │   │       interaction_constraints
│   │   │   │       learning_rate
│   │   │   │       max_bin
│   │   │   │       max_cat_threshold
│   │   │   │       max_cat_to_onehot
│   │   │   │       max_delta_step
│   │   │   │       max_depth
│   │   │   │       max_leaves
│   │   │   │       min_child_weight
│   │   │   │       missing
│   │   │   │       monotone_constraints
│   │   │   │       multi_strategy
│   │   │   │       num_parallel_tree
│   │   │   │       n_estimators
│   │   │   │       n_jobs
│   │   │   │       objective
│   │   │   │       random_state
│   │   │   │       reg_alpha
│   │   │   │       reg_lambda
│   │   │   │       sampling_method
│   │   │   │       scale_pos_weight
│   │   │   │       subsample
│   │   │   │       tree_method
│   │   │   │       validate_parameters
│   │   │   │       verbosity
│   │   │   │
│   │   │   └───tags
│   │   │           mlflow.log-model.history
│   │   │           mlflow.runName
│   │   │           mlflow.source.git.commit
│   │   │           mlflow.source.name
│   │   │           mlflow.source.type
│   │   │           mlflow.user
│   │   │
│   │   ├───7c1c84bf47c2441a9168bdb8c7ca4df4
│   │   │   │   meta.yaml
│   │   │   │
│   │   │   ├───artifacts
│   │   │   │   └───random_forest_apartments
│   │   │   │           conda.yaml
│   │   │   │           MLmodel
│   │   │   │           model.pkl
│   │   │   │           python_env.yaml
│   │   │   │           requirements.txt
│   │   │   │
│   │   │   ├───metrics
│   │   │   │       train_r2
│   │   │   │       val_mse
│   │   │   │       val_r2
│   │   │   │
│   │   │   ├───params
│   │   │   │       bootstrap
│   │   │   │       ccp_alpha
│   │   │   │       criterion
│   │   │   │       max_depth
│   │   │   │       max_features
│   │   │   │       max_leaf_nodes
│   │   │   │       max_samples
│   │   │   │       min_impurity_decrease
│   │   │   │       min_samples_leaf
│   │   │   │       min_samples_split
│   │   │   │       min_weight_fraction_leaf
│   │   │   │       n_estimators
│   │   │   │       n_jobs
│   │   │   │       oob_score
│   │   │   │       random_state
│   │   │   │       verbose
│   │   │   │       warm_start
│   │   │   │
│   │   │   └───tags
│   │   │           mlflow.log-model.history
│   │   │           mlflow.runName
│   │   │           mlflow.source.git.commit
│   │   │           mlflow.source.name
│   │   │           mlflow.source.type
│   │   │           mlflow.user
│   │   │
│   │   └───f3effa10adbc48568ca336150998e125
│   │       │   meta.yaml
│   │       │
│   │       ├───artifacts
│   │       │   └───catboost_apartments
│   │       │           conda.yaml
│   │       │           MLmodel
│   │       │           model.pkl
│   │       │           python_env.yaml
│   │       │           requirements.txt
│   │       │
│   │       ├───metrics
│   │       │       train_r2
│   │       │       val_mse
│   │       │       val_r2
│   │       │
│   │       ├───params
│   │       │       loss_function
│   │       │       verbose
│   │       │
│   │       └───tags
│   │               mlflow.log-model.history
│   │               mlflow.runName
│   │               mlflow.source.git.commit
│   │               mlflow.source.name
│   │               mlflow.source.type
│   │               mlflow.user
│   │
│   └───models
├───models
│       catboost_apartments.pkl
│       catboost_rent.pkl
│       lightgbm_apartments.pkl
│       lightgbm_rent.pkl
│       random_forest_apartments.pkl
│       random_forest_rent.pkl
│       xgboost_apartments.pkl
│       xgboost_rent.pkl
│
├───notebooks
│       eda.ipynb
│       eda_processed_file.ipynb
│
└───src
    ├───data
    │   │   data_utils.py
    │   │   load_data.py
    │   │   preprocess_data.py
    │   │
    │   └───__pycache__
    │           data_utils.cpython-38.pyc
    │           load_data.cpython-38.pyc
    │
    └───models
            evaluate_model.py
            predict.py
            run_all_experiments.py
            train_model.py