# DeepDL drug-likeness scoring

Scores drug-likeness with DeepDL, a SMILES recurrent neural network language model that Lee and colleagues at KAIST trained only on approved drugs, so no set of non-drugs has to be assembled and no arbitrary negative class biases the result. The score is 100 plus the log-likelihood of the molecule under that model, giving a ceiling of 100 and higher values for chemistry resembling marketed drugs. It behaved more consistently than two-class classifiers across diverse test sets, but very short SMILES score spuriously high and the number is not a probability of approval.

This model was incorporated on 2024-09-04.Last packaged on 2026-04-23.

## Information
### Identifiers
- **Ersilia Identifier:** `eos9p4a`
- **Slug:** `deep-dl`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Drug-likeness`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Single drug-likeness score topping out at 100, with higher values meaning stronger resemblance to approved drugs.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| druglikeness_score | float | high | Druglikeness score in the range of 0 to 100 |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos9p4a](https://hub.docker.com/r/ersiliaos/eos9p4a)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9p4a.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9p4a.zip)

### Resource Consumption
- **Model Size (Mb):** `187`
- **Environment Size (Mb):** `1266`
- **Image Size (Mb):** `1496.28`

**Computational Performance (seconds):**
- 10 inputs: `32.71`
- 100 inputs: `35.65`
- 10000 inputs: `517.14`

### References
- **Source Code**: [https://github.com/SeonghwanSeo/DeepDL](https://github.com/SeonghwanSeo/DeepDL)
- **Publication**: [https://doi.org/10.1039/D1SC05248A](https://doi.org/10.1039/D1SC05248A)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2022`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [None](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos9p4a
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos9p4a
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
