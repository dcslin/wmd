#!/bin/bash
python gen_sample_data.py
python get_word_vectors.py sample_news.txt sample_news_vec.pk sample_news_vec.mat
python wmd.py sample_news_vec.pk sample_news_wmd_d.pk
python get_cluster.py
