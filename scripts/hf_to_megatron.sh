export MEGATRON_LM_PATH='/home/jovyan/luochenyu01/ms_swift_all_train/pretrain/Megatron-LM/Megatron-LM-core_v0.13.0'
# Dense, MoE model path
model_path=""
output_dir=""
swift export \
    --model $model_path \
    --to_mcore true \
    --torch_dtype bfloat16 \
    --output_dir $output_dir \
    --test_convert_precision true
