# BuggyAI_Source
This is the main repository for the BuggyAI Code. We have split code for this repository by where it is used in a production environment.

Under the Server_Code directory is a Flask REST API which resides on an Ubuntu 18.04 server using Nginx as a Reverse Proxy in front of Gunicorn which runs the Flask app.

Under the (insert directory here) directory is the actual training and testing code for our model.


--- Credits To ---

[Xiaoping Wu and Team] -- For granting permission to use the IP102 dataset. Our project does not use any pretrained models or other source code, as we have developed and trained our own for our own purposes. We have only used the image dataset in training and validating our own model.

@inproceedings{Wu2019Insect,
  title={IP102: A Large-Scale Benchmark Dataset for Insect Pest Recognition},
  author={Xiaoping Wu and Chi Zhan and Yukun Lai and Ming-Ming Cheng and Jufeng Yang},
  booktitle={IEEE CVPR},
  pages={8787--8796},
  year={2019},
}