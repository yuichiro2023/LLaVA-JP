from huggingface_hub import HfApi

# APIインスタンスの作成
api = HfApi()

# アップロードするローカルフォルダのパス
local_folder_path = "./output_llava/checkpoints/finetune_gpt2_rinna_small-v1-siglip-so400m-patch14-384/checkpoint-2000"

# アップロード先のリポジトリ情報
repo_id = "hibikaze/finetune_gpt2_rinna_small-v1-siglip-so400m-patch14-384_checkpoint-2000"  # リポジトリID（Hugging Face Hubのユーザー名とリポジトリ名）
repo_type = "model"  # リポジトリの種類（"model", "dataset", "space"など）
commit_message = "upload model"  # コミットメッセージ

# アップロード処理
api.upload_folder(
    folder_path=local_folder_path,
    repo_id=repo_id,
    repo_type=repo_type,
    commit_message=commit_message,
    ignore_patterns=[
        "runs",
        "log",
        "training_args.bin",
        "global_step*",
        "latest",
        "rng_state.pth",
        "rng_state_*.pth",
        "scheduler.pt",
        "trainer_state.json",
        "zero_to_fp32.py",
        "optimizer.pt",
    ],
)
