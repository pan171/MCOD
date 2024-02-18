MCOD
The implementation for "Unsupervised Outlier Detection Using Memory and Contrastive Learning"
https://ieeexplore.ieee.org/document/9913887



```
conda create -n mcod python=3.8
source activate mcod


pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html

pip install -r requirements.txt
```


If you find this work useful in your research, please consider citing:

    @ARTICLE{9913887,
      author={Huyan, Ning and Quan, Dou and Zhang, Xiangrong and Liang, Xuefeng and Chanussot, Jocelyn and Jiao, Licheng},
      journal={IEEE Transactions on Image Processing}, 
      title={Unsupervised Outlier Detection Using Memory and Contrastive Learning}, 
      year={2022},
      volume={31},
      number={},
      pages={6440-6454},
      doi={10.1109/TIP.2022.3211476}}
