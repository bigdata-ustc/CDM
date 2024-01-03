# coding: utf-8
# 2024/1/3 @ Gao Weibo

import pytest
import pandas as pd
import random


@pytest.fixture(scope="package")
def meta():
    meta_data = {'userId': ['001', '002', '003'], 'itemId': ['adf', 'w5'], 'skill': ['skill1', 'skill2', 'skill3', 'skill4']}
    return meta_data


@pytest.fixture(scope="package")
def data(meta):
    meta_data = meta

    userIds, itemIds, responses = [], [], []
    for user in meta_data['userId']:
        for i, item in enumerate(meta_data['itemId']):
            userIds.append(user)
            itemIds.append(item)
            responses.append(random.randint(0, 1))

    df_data = pd.DataFrame({'userId': userIds, 'itemId': itemIds, 'response': responses})
    return df_data