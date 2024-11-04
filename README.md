# Relevance Aware Algorithmic Recourse (RAAR)

This code was used to research how "relevance" affects algorithmic recourse. There are many regression based datasets contained, and the ones specifically used in the paper are calHousing, debutenizer, deltaAilerons, elecLen1, housingBoston, insurance, kinematics32fh, kinematics8fh, mortgage, space_ga, sulfur, treasury, triazines, wages, wine.

Results show that relevance contributes recourses comparable to well-known baselines, with greater efficiency and lower relative costs.

## Setup
Note: only works on x86_64 versions of python. You can use conda on MacOS to mitigate this. 

```bash
# required for IRonPy which generates the relevance functions
export SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True 

# required packages
pip install pandas
pip install IRonPy
pip install matplotlib
pip install lightgbm
pip install bayesian-optimization
pip install scikit-learn
```

## 1. Usage (algorithmic recourse)
This runs algorithmic recourse.

- Specify absolute path to store recourses
- **You must also put the features as arguments for the bayesian optimization**
- In preprocessing data, you can use the provided encoder function for supported datasets, or encode directly through the manually_label_categorical_data function

Run get_algorithmic_recourse_results(dataset_name, model_type, step_size, isglobal, local_multiplier_target) 

More information is listed in the code.

## 2. Usage (processing algorithmic recourse results)
This generates a summary of your algorithmic recourse into a csv file.\
Run process_results(dataset_names, models, file_path_intermediate, file_path_result, is_global, local_multiplier_target, step_size).

More information is listed in the code.


## License

[MIT](https://choosealicense.com/licenses/mit/)
