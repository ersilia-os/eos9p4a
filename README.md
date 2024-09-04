# Drug-likeness scoring based on unsupervised learning

This model evaluates drug-likeness using an unsupervised learning approach, eliminating the need for labeled data and avoiding biases from incomplete negative sets. It extracts features directly from known drug molecules, identifying common characteristics through a recurrent neural network (RNN) language model. By representing molecules as SMILES strings, the model learns the probability distribution of known drugs and assesses new molecules based on their likelihood of appearing in this space. This method offers a robust and consistent evaluation of drug-likeness, outperforming traditional supervised models like TCC in generalization across various datasets.

## Identifiers

* EOS model ID: `eos9p4a`
* Slug: `deep-dl`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Regression`
* Output: `Score`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Higher score indicates higher drug likeness

## References

* [Publication](https://pubs.rsc.org/en/content/articlehtml/2022/sc/d1sc05248a)
* [Source Code](https://github.com/SeonghwanSeo/DeepDL)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos9p4a)

## Citation

If you use this model, please cite the [original authors](https://pubs.rsc.org/en/content/articlehtml/2022/sc/d1sc05248a) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a GPL-3.0-or-later license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!