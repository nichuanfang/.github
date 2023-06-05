## 集中管理同一个账户下的变量和密钥

>使用步骤

1.  编辑[`config.json`](https://github.com/nichuanfang/.github/blob/main/config.json)
```
topic: 当前区块的主要分类
repositories: 配置的变量和密钥应用到哪些仓库
vars: 全局变量   通过 ${{ vars.变量名  }} 调用
secrets: 全局密钥   通过 ${{ secrets.密钥名 }} 调用
```

2. 手动触发工作流 [`generate and sync`](https://github.com/nichuanfang/.github/actions/workflows/main.yml)

3. your project-> Settings -> Secrets and variables -> config your secrets and variables

4. 生成的[`synchronize_secrets.yml`](https://github.com/nichuanfang/.github/blob/main/.github/workflows/synchronize_secrets.yml)和[`synchronize_variables.yml`](https://github.com/nichuanfang/.github/blob/main/.github/workflows/synchronize_variables.yml)为两个新的工作流
```
synchronize_variables.yml: 同步全局变量
synchronize_secrets.yml: 同步全局密钥
```
