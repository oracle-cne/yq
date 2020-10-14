This oracle-template should automatically onboard new upstream yq releases into the yq pipeline.
Tag format as specified in template.yaml is as follows.

* major: [0-9] - a single character in the range between 0 & 9
* minor: [0-9]+ - double digit version in the range between 0 & 9
* patch: [[:digit:]]+ - [:digit:] matches a digit [0-9]; + Quantifier - matches between one and unlimited times

