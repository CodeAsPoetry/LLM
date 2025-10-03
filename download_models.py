# coding = "utf-8"
from modelscope.hub.snapshot_download import snapshot_download
# pretrain models
# Dense model: Qwen/Qwen3-8B-Base, Qwen/Qwen3-4B-Base
# Moe model: Qwen/Qwen3-30B-A3B-Base

# post-training models
# Dense model: Qwen/Qwen3-8B, Qwen/Qwen3-4B
# Moe model: Qwen/Qwen3-30B-A3B

# Reward models
# Skywork/Skywork-Reward-V2-Qwen3-4B

model_dir = snapshot_download(model_id="Qwen/Qwen3-30B-A3B-Base", local_dir="/Users/codeaspoetry/WorkDesk/LLM/models/Qwen3/Qwen3-30B-A3B-Base")
