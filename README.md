# OpenAI Gym

[OpenAI](https://openai.com/research/openai-gym-beta) [Gym](https://github.com/openai/gym) has been migrated to [Gymnasium](https://github.com/Farama-Foundation/Gymnasium). Visit [Migration Guide](https://gymnasium.farama.org/content/migration-guide/) for more information. Also check [Gym Docs](https://www.gymlibrary.dev/) and [Gymnasium Docs](https://gymnasium.farama.org/) to compare what changed.

```
import gymnasium as gym
```

Package versions used
```
python		3.11.5
pip		23.3
wheel		0.41.2
setuptools	68.0.0
tqdm		4.65.0
seaborn		0.12.2
notebook	6.5.4
matplotlib	3.8.0
gymnasium	0.28.1
swig		4.1.1.post0
```

First create [conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) environment with python 3.11
```
conda create --name condagym python=3.11
```

Activate the environment
```
conda activate condagym
```

Then setup python interpreter in PyCharm project settings. Finally, install the requirements
```
pip install -r requirements.txt
```