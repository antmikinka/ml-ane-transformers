





class correct_for_bias_scale_order_inversion(state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys,
                                              error_msgs):
                                                state_dict[prefix + 'bias'] = state_dict[prefix + 'bias'] / state_dict[prefix + 'weight']
                                                return state_dict

class LayerNormANE(LayerNormANE):
  






class MultiHeadSelfAttention(modeling_llama.MultiHeadSelfAttention):
  """Not sure if MultiHeadSelfAttention is optimized for ANE
  """
  def __init__(self, config):
    super().__init__(config)

    setattr(
      self, 'q_lin',
      nn.Conv2d(
        in_channels=
