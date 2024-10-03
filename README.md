## Goal
- This project is based on deeplearning.ai's [AI Python for Beginners series](https://learn.deeplearning.ai/courses/ai-python-for-beginners).
- The main objective is to provide an alternative for learners who can't access the OpenAI API.
- We use the free GLM4 Flash API to run the AI Python for Beginners series locally.
- I've also created study buddy agents on [智谱清言](https://chatglm.cn/) to assist learners:
  - Season 1: [Learn Python with Andrew Ng - Study Buddy](https://chatglm.cn/main/gdetail/66ba050ebf79f88056ba4fa5?lang=en)
  - Season 2: [Learn Python with Andrew Ng (Season 2) - Study Buddy](https://chatglm.cn/main/gdetail/66d576c2e27e9d7acf9fd04f?lang=en)
  - Seasons 3 & 4: [Learn Python with Andrew Ng (Seasons 3 & 4) - Study Buddy](https://chatglm.cn/main/gdetail/66ed17f4c11b5e859c1e82e3?lang=en)

## Prerequisites
- You need Python (with certain packages) and Jupyter Notebook installed on your computer.
  - Refer to [Installing_Python.ipynb](https://github.com/nicky-aigc/AI-Python-For-Beginners-with-GLM4/blob/main/S4/L7/Installing_Python.ipynb) for installation instructions.
  - If a package is missing, simply install it using pip.
- Create an `.env` file in the same directory as the tutorial notebook with the following content:
  ```
  OPENAI_API_KEY="your_zhipu_api_key" # Replace with your actual ZhiPu API key
  ```

## Getting Your ZhiPu API Key
- To access the ZhiPu API, visit [https://bigmodel.cn/](https://bigmodel.cn/)
- Sign up for a free account to obtain your API key.

## Modified Materials (Compatible with GLM4 Flash API)
- S1: AI Python for Beginners: [Basics of AI Python Coding](https://github.com/nicky-aigc/AI-Python-For-Beginners-with-GLM4/tree/main/S1)
- S2: AI Python for Beginners: [Automating Tasks with Python](https://github.com/nicky-aigc/AI-Python-For-Beginners-with-GLM4/tree/main/S2)
- S3: AI Python for Beginners: [Working with Your Own Data and Documents in Python](https://github.com/nicky-aigc/AI-Python-For-Beginners-with-GLM4/tree/main/S3)
- S4: AI Python for Beginners: [Extending Python with Packages and APIs](https://github.com/nicky-aigc/AI-Python-For-Beginners-with-GLM4/tree/main/S4)

## Important Notes
- Check the `helper_functions.py` file for each lesson, as it often contains valuable information.
- While the GLM4 Flash API is currently free, you can adjust the `model` parameter in `helper_functions.py` for higher-quality content generation.
- For available models, refer to [https://bigmodel.cn/dev/api/normal-model/glm-4](https://bigmodel.cn/dev/api/normal-model/glm-4)

---

中文:

---

## 目标
- 本项目基于 deeplearning.ai 的 [AI Python for Beginners 系列课程](https://learn.deeplearning.ai/courses/ai-python-for-beginners)。
- 主要目的是为无法使用 OpenAI API 的学习者提供替代方案。
- 我们使用免费的 GLM4 Flash API 在本地运行 AI Python for Beginners 系列课程。
- 我还在[智谱清言](https://chatglm.cn/)上创建了学习助手：
  - 第一季：[【伴学】跟吴恩达老师学Python](https://chatglm.cn/main/gdetail/66ba050ebf79f88056ba4fa5)
  - 第二季：[【伴学】跟吴恩达老师学Python第二季](https://chatglm.cn/main/gdetail/66d576c2e27e9d7acf9fd04f)
  - 第三、四季：[【伴学】跟吴恩达老师学Python三四季](https://chatglm.cn/main/gdetail/66ed17f4c11b5e859c1e82e3)

## 前提条件
- 您需要在电脑上安装 Python（及相关包）和 Jupyter Notebook。
  - 安装指南请参考 [Installing_Python.ipynb](https://github.com/nicky-aigc/AI-Python-For-Beginners-with-GLM4/blob/main/S4/L7/Installing_Python.ipynb)。
  - 如缺少某个包，只需使用 pip 安装即可。
- 在教程笔记本所在目录创建一个 `.env` 文件，内容如下：
  ```
  OPENAI_API_KEY="your_zhipu_api_key" # 替换为您的实际智谱 API 密钥
  ```

## 获取智谱 API 密钥
- 访问 [https://bigmodel.cn/](https://bigmodel.cn/) 以使用智谱 API。
- 注册免费账号以获取 API 密钥。

## 修改后的教材（适用于 GLM4 Flash API）
- S1: AI Python for Beginners: [Python AI 编程基础](https://github.com/nicky-aigc/AI-Python-For-Beginners-with-GLM4/tree/main/S1)
- S2: AI Python for Beginners: [Python 自动化任务](https://github.com/nicky-aigc/AI-Python-For-Beginners-with-GLM4/tree/main/S2)
- S3: AI Python for Beginners: [Python 处理个人数据和文档](https://github.com/nicky-aigc/AI-Python-For-Beginners-with-GLM4/tree/main/S3)
- S4: AI Python for Beginners: [使用包和 API 扩展 Python](https://github.com/nicky-aigc/AI-Python-For-Beginners-with-GLM4/tree/main/S4)

## 注意事项
- 每节课的 `helper_functions.py` 文件通常包含有用的信息，请务必查看。
- 目前 GLM4 Flash API 是免费的，如需更高质量的模型生成内容，可在 `helper_functions.py` 中调整 `model` 参数。
- 可用模型请参考 [https://bigmodel.cn/dev/api/normal-model/glm-4](https://bigmodel.cn/dev/api/normal-model/glm-4)
