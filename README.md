# Drug-likeness scoring based on unsupervised learning

This model evaluates drug-likeness using an unsupervised learning approach, eliminating the need for labeled data and avoiding biases from incomplete negative sets. It extracts features directly from known drug molecules, identifying common characteristics through a recurrent neural network (RNN) language model. By representing molecules as SMILES strings, the model learns the probability distribution of known drugs and assesses new molecules based on their likelihood of appearing in this space. This method offers a robust and consistent evaluation of drug-likeness, outperforming traditional supervised models like TCC in generalization across various datasets.

This model was incorporated on 2024-09-04.

## Information
### Identifiers
- **Ersilia Identifier:** `eos9p4a`
- **Slug:** `deep-dl`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Drug-likeness`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Higher score indicates higher drug likeness

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
- **Environment Size (Mb):** `1260`
- **Image Size (Mb):** `1458.73`


### References
- **Source Code**: [https://github.com/SeonghwanSeo/DeepDL](https://github.com/SeonghwanSeo/DeepDL)
- **Publication**: [https://pubs.rsc.org/en/content/articlehtml/2022/sc/d1sc05248a](https://pubs.rsc.org/en/content/articlehtml/2022/sc/d1sc05248a)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2022`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-or-later](LICENSE) license.

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
