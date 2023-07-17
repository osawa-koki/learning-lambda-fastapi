# learning-lambda-fastapi

😮‍💨😮‍💨😮‍💨 LambdaでFastAPIを動かす！  

![成果物](./docs/img/fruit.gif)  

## 開発環境の構築方法

最初にAWS CLIをインストールします。  
<https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/install-cliv2.html>  

以下のコマンドを実行して、AWS CLIのバージョンが表示されればOKです。  

```shell
aws --version
```

認証情報を設定します。  

```shell
aws configure
```

以下のように聞かれるので、適宜入力してください。

```shell
AWS Access Key ID [None]: アクセスキーID
AWS Secret Access Key [None]: シークレットアクセスキー
Default region name [None]: リージョン名
Default output format [None]: json
```

これらの情報は、AWSのコンソール画面から確認できます。  
IAMのページから指定のユーザを選択肢、アクセスキーを発行してください。  

続いて、AWS SAMをインストールします。  
こちらはサーバレスアプリケーションを構築するためのツールです。  
<https://docs.aws.amazon.com/ja_jp/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html>  

以下のコマンドを実行して、AWS SAMのバージョンが表示されればOKです。  

```shell
sam --version
```

サーバサイドアプリケーションを開発用に実行するためには、以下のコマンドを実行します。  
ビルドにはDockerが必要です。  

```shell
sam build
sam local start-api
```

<http://localhost:3000>にリクエストを投げて、`{"message":"Hello GET."}`が返ってくればOKです。  

各、イベントを発火させるには、以下のコマンドを実行します。  

```shell
sam local invoke --event <イベントファイルまでのパス> <関数名>

# 例
sam local invoke --event ./events/get.json GetFunction
```

## 本番環境の準備

### GitHub Secretsの設定

| キー | バリュー |
| --- | --- |
| PROJECT_NAME | プロジェクト名(CloudFormationのスタック名) |
| AWS_ACCESS_KEY_ID | AWSのアクセスキーID |
| AWS_SECRET_ACCESS_KEY | AWSのシークレットアクセスキー |
| AWS_REGION | リージョン名 |

## 環境情報

| 環境 | バージョン |
| --- | --- |
| Node.js | v18.12.1 |
| AWS CLI | 2.11.16 |
| SAM CLI | 1.82.0 |
