# Ansible Playbook for Mastodon

多言語：  
[English](README.md)

## 概要

このAnsibleプレイブックは分散型SNS「[マストドン](https://joinmastodon.org/)」を構築・運用するためのものです。

マストドン公式は[Ansibleで自動化するためのリポジトリを公開](https://github.com/mastodon/mastodon-ansible)していますが、ここ数年ほとんどアップデートされていません。

また、とても特殊な書き方をしておりAnsibleベストプラクティスに基づいていないために保守性や拡張性がありません。

このプロジェクトの目標は、マストドンサーバを運用するための新しいプレイブックを公開することにあります。