def addRightSideToList(l):
    '''
    doesn't work because order matters
    '''
    toAdd = []
    for item in l:
        if 'LT_' in item:
            toAdd.append(item.replace('LT_', 'RT_'))
    return l + toAdd

# to switch off an action,
# just add '-' or something so it won't run
build_actions = ['-bind',
                 '-sec_motion_system',
                 'primary_ctl_system_first',
                 '-primary_ctl_system_second',
                 '-load_weights',
                 '-clean',
                 '-surface_constraint',
                 '-eyes',
                 '-eyeballs']

# bnds to attach to surface
slidingBnds = [u'LT_upperPinch_outCrease_bnd',
u'LT_corner_outCrease_bnd',
u'LT_lowerCorner_outCrease_bnd',
u'LT_corner_cheek_bnd',
u'LT_outerB_cheekB_bnd',
u'LT_lowerSneer_outCrease_bnd',
u'CT_lower_midCrease_bnd',
u'CT_lower_cheek_bnd',
u'LT_lowerSide_outCrease_bnd',
u'LT_lowerPinch_lip_bnd',
u'LT_upperSide_lip_bnd',
u'CT_lower_lip_bnd',
u'LT_lowerSneer_lip_bnd',
u'LT_corner_lip_bnd',
u'LT_lowerSide_lip_bnd',
u'CT_upper_lip_bnd',
u'LT_upperPinch_lip_bnd',
u'LT_upperSneer_lip_bnd',
u'LT_lowerOuter_eyeSocket_bnd',
u'LT_lowerPinch_cheek_bnd',
u'LT_lowerInner_eyeSocket_bnd',
u'LT_lower_eyeSocket_bnd',
u'LT_upperSide_inCrease_bnd',
u'CT_lower_inCrease_bnd',
u'LT_lowerSide_inCrease_bnd',
u'CT_upper_cheek_bnd',
u'CT_upper_inCrease_bnd',
u'LT_lowerPinch_inCrease_bnd',
u'LT_upperPinch_inCrease_bnd',
u'LT_lowerSide_midCrease_bnd',
u'LT_lowerSide_cheek_bnd',
u'LT_upperCorner_cheek_bnd',
u'LT_lowerCorner_cheek_bnd',
u'LT_outerB_cheekA_bnd',
u'LT_outerB_cheekC_bnd',
u'LT_lowerPinch_midCrease_bnd',
u'LT_lowerSneer_cheek_bnd',
u'LT_lowerPinch_outCrease_bnd',
u'LT_outerB_cheekD_bnd',
u'CT_upper_midCrease_bnd',
u'CT_upper_outCrease_bnd',
u'LT_upperSide_midCrease_bnd',
u'LT_upperSide_outCrease_bnd',
u'LT_upperSneer_inCrease_bnd',
u'LT_upperSneer_midCrease_bnd',
u'LT_upperSneer_outCrease_bnd',
u'LT_upperPinch_midCrease_bnd',
u'CT_lower_outCrease_bnd',
u'LT_lowerSneer_inCrease_bnd',
u'LT_lowerSneer_midCrease_bnd',
u'LT_upperCorner_lip_bnd',
u'LT_lowerCorner_lip_bnd',
u'LT_upperCorner_inCrease_bnd',
u'LT_upperCorner_midCrease_bnd',
u'LT_upperCorner_outCrease_bnd',
u'LT_corner_inCrease_bnd',
u'LT_corner_midCrease_bnd',
u'LT_lowerCorner_inCrease_bnd',
u'LT_lowerCorner_midCrease_bnd',
u'LT_mid_browA_bnd',
u'LT_out_browA_bnd',
u'LT_outerB_temple_bnd',
u'LT_outerB_squint_bnd',
u'CT_mid_forehead_bnd',
u'LT_outerA_temple_bnd',
u'LT_in_browA_bnd',
u'LT_upper_eyeSocket_bnd',
u'LT_upperInner_eyeSocket_bnd',
u'LT_upperOuter_eyeSocket_bnd',
u'LT_outer_eyeSocket_bnd',
u'LT_inner_eyeSocket_bnd',
u'CT_mid_temple_bnd',
u'CT_mid_squint_bnd',
u'LT_outerA_squint_bnd',
u'LT_side_forehead_bnd',
u'LT_outerA_forehead_bnd',
u'LT_outerB_forehead_bnd',
u'LT_outerC_cheekB_bnd',
u'LT_outerC_cheekA_bnd',
u'LT_outerC_cheekC_bnd',
u'LT_outerC_cheekD_bnd',
u'LT_outerC_temple_bnd',
u'LT_outerC_squint_bnd',
u'LT_outerC_forehead_bnd',
u'RT_upperPinch_outCrease_bnd',
u'RT_corner_outCrease_bnd',
u'RT_lowerCorner_outCrease_bnd',
u'RT_corner_cheek_bnd',
u'RT_outerB_cheekB_bnd',
u'RT_lowerSneer_outCrease_bnd',
u'RT_lowerSide_outCrease_bnd',
u'RT_lowerPinch_lip_bnd',
u'RT_upperSide_lip_bnd',
u'RT_lowerSneer_lip_bnd',
u'RT_corner_lip_bnd',
u'RT_lowerSide_lip_bnd',
u'RT_upperPinch_lip_bnd',
u'RT_upperSneer_lip_bnd',
u'RT_lowerOuter_eyeSocket_bnd',
u'RT_lowerPinch_cheek_bnd',
u'RT_lowerInner_eyeSocket_bnd',
u'RT_lower_eyeSocket_bnd',
u'RT_upperSide_inCrease_bnd',
u'RT_lowerSide_inCrease_bnd',
u'RT_lowerPinch_inCrease_bnd',
u'RT_upperPinch_inCrease_bnd',
u'RT_lowerSide_midCrease_bnd',
u'RT_lowerSide_cheek_bnd',
u'RT_upperCorner_cheek_bnd',
u'RT_lowerCorner_cheek_bnd',
u'RT_outerB_cheekA_bnd',
u'RT_outerB_cheekC_bnd',
u'RT_lowerPinch_midCrease_bnd',
u'RT_lowerSneer_cheek_bnd',
u'RT_lowerPinch_outCrease_bnd',
u'RT_outerB_cheekD_bnd',
u'RT_upperSide_midCrease_bnd',
u'RT_upperSide_outCrease_bnd',
u'RT_upperSneer_inCrease_bnd',
u'RT_upperSneer_midCrease_bnd',
u'RT_upperSneer_outCrease_bnd',
u'RT_upperPinch_midCrease_bnd',
u'RT_lowerSneer_inCrease_bnd',
u'RT_lowerSneer_midCrease_bnd',
u'RT_upperCorner_lip_bnd',
u'RT_lowerCorner_lip_bnd',
u'RT_upperCorner_inCrease_bnd',
u'RT_upperCorner_midCrease_bnd',
u'RT_upperCorner_outCrease_bnd',
u'RT_corner_inCrease_bnd',
u'RT_corner_midCrease_bnd',
u'RT_lowerCorner_inCrease_bnd',
u'RT_lowerCorner_midCrease_bnd',
u'RT_mid_browA_bnd',
u'RT_out_browA_bnd',
u'RT_outerB_temple_bnd',
u'RT_outerB_squint_bnd',
u'RT_outerA_temple_bnd',
u'RT_in_browA_bnd',
u'RT_upper_eyeSocket_bnd',
u'RT_upperInner_eyeSocket_bnd',
u'RT_upperOuter_eyeSocket_bnd',
u'RT_outer_eyeSocket_bnd',
u'RT_inner_eyeSocket_bnd',
u'RT_outerA_squint_bnd',
u'RT_side_forehead_bnd',
u'RT_outerA_forehead_bnd',
u'RT_outerB_forehead_bnd',
u'RT_outerC_cheekB_bnd',
u'RT_outerC_cheekA_bnd',
u'RT_outerC_cheekC_bnd',
u'RT_outerC_cheekD_bnd',
u'RT_outerC_temple_bnd',
u'RT_outerC_squint_bnd',
u'RT_outerC_forehead_bnd']

# list of priCtls for first pass
# order is important
# those created earlier can be affected by those created later
# only need to specify LT and CT - RT is added in all_bnds_for_priCtls

bnds_for_priCtls = [u'CT__mouthMover_pLoc',
                    u'CT__jaw_pLoc',
                    u'LT_corner_lip_pLoc']

all_bnds_for_priCtls = addRightSideToList(bnds_for_priCtls)

priCtlMappings = {u'CT__jaw_pri_ctrl': {u'CT__chin_bnd': 0.485,
                       u'CT__jaw_bnd': 1.0,
                       u'CT__neck_bnd': 0.04,
                       u'CT_lower_lip_bnd': 1.0,
                       u'CT_mid_chin_bnd': 0.9,
                       u'CT_upper_lip_bnd': 0.01,
                       u'LT__chinA_bnd': 0.325,
                       u'LT__chin_bnd': 0.41,
                       u'LT__neckA_bnd': 0.025,
                       u'LT__neckB_bnd': 0.02,
                       u'LT__neck_bnd': 0.03,
                       u'LT__sneer_bnd': 0.075,
                       u'LT_cornerLow_jaw_bnd': 0.1,
                       u'LT_cornerUp_jaw_bnd': 0.1,
                       u'LT_corner_jaw_bnd': 0.1,
                       u'LT_corner_lip_bnd': 0.5,
                       u'LT_corner_sneer_bnd': 0.25,
                       u'LT_in_chin_bnd': 0.46,
                       u'LT_in_neck_bnd': 0.04,
                       u'LT_lowOut_cheek_bnd': 0.05,
                       u'LT_low_cheek_bnd': 0.2,
                       u'LT_low_crease_bnd': 0.5,
                       u'LT_low_jaw_bnd': 0.015,
                       u'LT_lowerCorner_lip_bnd': 0.6,
                       u'LT_lowerPinch_lip_bnd': 0.8,
                       u'LT_lowerSide_lip_bnd': 0.98,
                       u'LT_lowerSneer_lip_bnd': 0.925,
                       u'LT_midCorner_chin_bnd': 0.71,
                       u'LT_midLow_cheek_bnd': 0.3,
                       u'LT_midUp_cheek_bnd': 0.3,
                       u'LT_mid_cheek_bnd': 0.333,
                       u'LT_mid_chin_bnd': 0.855,
                       u'LT_mid_crease_bnd': 0.5,
                       u'LT_up_crease_bnd': 0.35,
                       u'LT_upperCorner_lip_bnd': 0.4,
                       u'LT_upperPinch_lip_bnd': 0.2,
                       u'LT_upperSide_lip_bnd': 0.025,
                       u'LT_upperSneer_lip_bnd': 0.075,
                       u'RT__chinA_bnd': 0.325,
                       u'RT__chin_bnd': 0.41,
                       u'RT__neckA_bnd': 0.025,
                       u'RT__neckB_bnd': 0.02,
                       u'RT__neck_bnd': 0.03,
                       u'RT__sneer_bnd': 0.075,
                       u'RT_cornerLow_jaw_bnd': 0.1,
                       u'RT_cornerUp_jaw_bnd': 0.1,
                       u'RT_corner_jaw_bnd': 0.1,
                       u'RT_corner_lip_bnd': 0.5,
                       u'RT_corner_sneer_bnd': 0.25,
                       u'RT_in_chin_bnd': 0.46,
                       u'RT_in_neck_bnd': 0.04,
                       u'RT_lowOut_cheek_bnd': 0.05,
                       u'RT_low_cheek_bnd': 0.2,
                       u'RT_low_crease_bnd': 0.5,
                       u'RT_low_jaw_bnd': 0.015,
                       u'RT_lowerCorner_lip_bnd': 0.6,
                       u'RT_lowerPinch_lip_bnd': 0.8,
                       u'RT_lowerSide_lip_bnd': 0.98,
                       u'RT_lowerSneer_lip_bnd': 0.925,
                       u'RT_midCorner_chin_bnd': 0.71,
                       u'RT_midLow_cheek_bnd': 0.3,
                       u'RT_midUp_cheek_bnd': 0.3,
                       u'RT_mid_cheek_bnd': 0.333,
                       u'RT_mid_chin_bnd': 0.855,
                       u'RT_mid_crease_bnd': 0.5,
                       u'RT_up_crease_bnd': 0.35,
                       u'RT_upperCorner_lip_bnd': 0.4,
                       u'RT_upperPinch_lip_bnd': 0.2,
                       u'RT_upperSide_lip_bnd': 0.025,
                       u'RT_upperSneer_lip_bnd': 0.075},
 u'CT__mouthMover_pri_ctrl': {u'CT__chin_bnd': 0.48,
                              u'CT__mouthMover_bnd': 1.0,
                              u'CT__neck_bnd': 0.04,
                              u'CT__sneer_bnd': 0.75,
                              u'CT_lower_lip_bnd': 1.0,
                              u'CT_mid_chin_bnd': 0.925,
                              u'CT_upper_lip_bnd': 1.0,
                              u'LT__chinA_bnd': 0.35,
                              u'LT__chin_bnd': 0.46,
                              u'LT__neckA_bnd': 0.025,
                              u'LT__neckB_bnd': 0.02,
                              u'LT__neck_bnd': 0.03,
                              u'LT__sneer_bnd': 0.75,
                              u'LT_cornerLow_jaw_bnd': 0.1,
                              u'LT_cornerUp_jaw_bnd': 0.1,
                              u'LT_corner_jaw_bnd': 0.1,
                              u'LT_corner_lip_bnd': 1.0,
                              u'LT_corner_sneer_bnd': 0.7,
                              u'LT_in_chin_bnd': 0.47,
                              u'LT_in_neck_bnd': 0.04,
                              u'LT_lowOut_cheek_bnd': 0.05,
                              u'LT_low_cheek_bnd': 0.25,
                              u'LT_low_crease_bnd': 0.7,
                              u'LT_low_jaw_bnd': 0.015,
                              u'LT_lowerCorner_lip_bnd': 1.0,
                              u'LT_lowerPinch_lip_bnd': 1.0,
                              u'LT_lowerSide_lip_bnd': 1.0,
                              u'LT_lowerSneer_lip_bnd': 1.0,
                              u'LT_midCorner_chin_bnd': 0.9,
                              u'LT_midLow_cheek_bnd': 0.45,
                              u'LT_midUp_cheek_bnd': 0.5,
                              u'LT_mid_cheek_bnd': 0.45,
                              u'LT_mid_chin_bnd': 0.9,
                              u'LT_mid_crease_bnd': 0.7,
                              u'LT_up_crease_bnd': 0.7,
                              u'LT_upperCorner_lip_bnd': 1.0,
                              u'LT_upperPinch_lip_bnd': 1.0,
                              u'LT_upperSide_lip_bnd': 1.0,
                              u'LT_upperSneer_lip_bnd': 1.0,
                              u'RT__chinA_bnd': 0.35,
                              u'RT__chin_bnd': 0.46,
                              u'RT__neckA_bnd': 0.025,
                              u'RT__neckB_bnd': 0.02,
                              u'RT__neck_bnd': 0.03,
                              u'RT__sneer_bnd': 0.75,
                              u'RT_cornerLow_jaw_bnd': 0.1,
                              u'RT_cornerUp_jaw_bnd': 0.1,
                              u'RT_corner_jaw_bnd': 0.1,
                              u'RT_corner_lip_bnd': 1.0,
                              u'RT_corner_sneer_bnd': 0.7,
                              u'RT_in_chin_bnd': 0.47,
                              u'RT_in_neck_bnd': 0.04,
                              u'RT_lowOut_cheek_bnd': 0.05,
                              u'RT_low_cheek_bnd': 0.25,
                              u'RT_low_crease_bnd': 0.7,
                              u'RT_low_jaw_bnd': 0.015,
                              u'RT_lowerCorner_lip_bnd': 1.0,
                              u'RT_lowerPinch_lip_bnd': 1.0,
                              u'RT_lowerSide_lip_bnd': 1.0,
                              u'RT_lowerSneer_lip_bnd': 1.0,
                              u'RT_midCorner_chin_bnd': 0.9,
                              u'RT_midLow_cheek_bnd': 0.45,
                              u'RT_midUp_cheek_bnd': 0.5,
                              u'RT_mid_cheek_bnd': 0.45,
                              u'RT_mid_chin_bnd': 0.9,
                              u'RT_mid_crease_bnd': 0.7,
                              u'RT_up_crease_bnd': 0.7,
                              u'RT_upperCorner_lip_bnd': 1.0,
                              u'RT_upperPinch_lip_bnd': 1.0,
                              u'RT_upperSide_lip_bnd': 1.0,
                              u'RT_upperSneer_lip_bnd': 1.0},
 u'CT_lower_lip_pri_ctrl': {u'CT_lower_lip_bnd': 1.0,
                            u'CT_mid_chin_bnd': 0.75,
                            u'LT_lowerPinch_lip_bnd': 0.3,
                            u'LT_lowerSide_lip_bnd': 0.95,
                            u'LT_lowerSneer_lip_bnd': 0.7,
                            u'LT_mid_chin_bnd': 0.5,
                            u'RT_lowerPinch_lip_bnd': 0.3,
                            u'RT_lowerSide_lip_bnd': 0.95,
                            u'RT_lowerSneer_lip_bnd': 0.7,
                            u'RT_mid_chin_bnd': 0.5},
 u'CT_upper_lip_pri_ctrl': {u'CT__sneer_bnd': 0.75,
                            u'CT_upper_lip_bnd': 1.0,
                            u'LT__sneer_bnd': 0.5,
                            u'LT_upperPinch_lip_bnd': 0.3,
                            u'LT_upperSide_lip_bnd': 0.95,
                            u'LT_upperSneer_lip_bnd': 0.7,
                            u'RT__sneer_bnd': 0.5,
                            u'RT_upperPinch_lip_bnd': 0.3,
                            u'RT_upperSide_lip_bnd': 0.95,
                            u'RT_upperSneer_lip_bnd': 0.7},
 u'LT__browMover_pri_ctrl': {u'CT__brow_bnd': 0.25,
                             u'LT__browMover_bnd': 1.0,
                             u'LT_in_browA_bnd': 0.8,
                             u'LT_in_browB_bnd': 1.0,
                             u'LT_in_browC_bnd': 1.0,
                             u'LT_mid_browA_bnd': 1.0,
                             u'LT_mid_browB_bnd': 0.9,
                             u'LT_out_browA_bnd': 0.8,
                             u'LT_out_browB_bnd': 0.8},
 u'LT__eyeMover_pri_ctrl': {u'CT__brow_bnd': 0.25,
                            u'CT__sneer_bnd': 0.25,
                            u'CT_low_eyeSocket_bnd': 0.25,
                            u'CT_mid_eyeSocket_bnd': 0.25,
                            u'CT_up_eyeSocket_bnd': 0.25,
                            u'LT__eyeMover_bnd': 1.0,
                            u'LT__sneer_bnd': 0.25,
                            u'LT__squint_bnd': 0.25,
                            u'LT_corner_sneer_bnd': 0.25,
                            u'LT_inCorner_eyeSocket_bnd': 1.0,
                            u'LT_in_cheek_bnd': 1.0,
                            u'LT_in_eyeSocket_bnd': 1.0,
                            u'LT_innerLower_eyelid_bnd': 1.0,
                            u'LT_innerUpper_eyelid_bnd': 1.0,
                            u'LT_inner_eyelid_bnd': 1.0,
                            u'LT_lower_eyelid_bnd': 1.0,
                            u'LT_midUp_cheek_bnd': 0.25,
                            u'LT_mid_eyeSocket_bnd': 1.0,
                            u'LT_outCorner_eyeSocket_bnd': 1.0,
                            u'LT_out_cheek_bnd': 1.0,
                            u'LT_out_eyeSocket_bnd': 1.0,
                            u'LT_outerLower_eyelid_bnd': 1.0,
                            u'LT_outerUpper_eyelid_bnd': 1.0,
                            u'LT_outer_eyelid_bnd': 1.0,
                            u'LT_up_cheek_bnd': 1.0,
                            u'LT_up_crease_bnd': 0.25,
                            u'LT_up_squint_bnd': 0.25,
                            u'LT_upper_eyelid_bnd': 1.0},
 u'LT__squint_pri_ctrl': {u'LT__sneer_bnd': 0.05,
                          u'LT__squint_bnd': 1.0,
                          u'LT_cornerLow_jaw_bnd': 0.05,
                          u'LT_cornerUp_jaw_bnd': 0.25,
                          u'LT_corner_jaw_bnd': 0.15,
                          u'LT_corner_sneer_bnd': 0.25,
                          u'LT_in_cheek_bnd': 0.25,
                          u'LT_low_crease_bnd': 0.05,
                          u'LT_midLow_cheek_bnd': 0.05,
                          u'LT_midUp_cheek_bnd': 0.5,
                          u'LT_mid_cheek_bnd': 0.15,
                          u'LT_mid_crease_bnd': 0.15,
                          u'LT_out_cheek_bnd': 0.85,
                          u'LT_up_cheek_bnd': 0.5,
                          u'LT_up_crease_bnd': 0.5,
                          u'LT_up_jaw_bnd': 0.3},
 u'LT_corner_lip_pri_ctrl': {u'CT__chin_bnd': 0.05,
                             u'CT__sneer_bnd': 0.1,
                             u'CT_lower_lip_bnd': 0.1,
                             u'CT_mid_chin_bnd': 0.1,
                             u'CT_upper_lip_bnd': 0.1,
                             u'LT__chinA_bnd': 0.175,
                             u'LT__chin_bnd': 0.25,
                             u'LT__sneer_bnd': 0.4,
                             u'LT_cornerLow_jaw_bnd': 0.075,
                             u'LT_cornerUp_jaw_bnd': 0.075,
                             u'LT_corner_jaw_bnd': 0.075,
                             u'LT_corner_lip_bnd': 1.0,
                             u'LT_corner_sneer_bnd': 0.8,
                             u'LT_in_chin_bnd': 0.15,
                             u'LT_in_forehead_bnd': 0.5,
                             u'LT_lowOut_cheek_bnd': 0.05,
                             u'LT_low_cheek_bnd': 0.15,
                             u'LT_low_crease_bnd': 0.65,
                             u'LT_lowerCorner_lip_bnd': 0.98,
                             u'LT_lowerPinch_lip_bnd': 0.785,
                             u'LT_lowerSide_lip_bnd': 0.3,
                             u'LT_lowerSneer_lip_bnd': 0.53,
                             u'LT_midCorner_chin_bnd': 0.85,
                             u'LT_midLow_cheek_bnd': 0.4,
                             u'LT_midUp_cheek_bnd': 0.4,
                             u'LT_mid_cheek_bnd': 0.52,
                             u'LT_mid_chin_bnd': 0.45,
                             u'LT_mid_crease_bnd': 0.75,
                             u'LT_up_crease_bnd': 0.6,
                             u'LT_upperCorner_lip_bnd': 0.98,
                             u'LT_upperPinch_lip_bnd': 0.785,
                             u'LT_upperSide_lip_bnd': 0.3,
                             u'LT_upperSneer_lip_bnd': 0.53},
 u'LT_in_browA_pri_ctrl': {u'CT__brow_bnd': 0.5,
                           u'LT_in_browA_bnd': 1.0,
                           u'LT_in_browB_bnd': 0.65,
                           u'LT_in_browC_bnd': 0.4,
                           u'LT_mid_browA_bnd': 0.15},
 u'LT_lowerSneer_lip_pri_ctrl': {u'CT_lower_lip_bnd': 0.5,
                                 u'CT_mid_chin_bnd': 0.35,
                                 u'LT_lowerPinch_lip_bnd': 0.5,
                                 u'LT_lowerSide_lip_bnd': 0.9,
                                 u'LT_lowerSneer_lip_bnd': 1.0,
                                 u'LT_mid_chin_bnd': 0.5,
                                 u'RT_lowerSide_lip_bnd': 0.1},
 u'LT_lower_eyelid_pri_ctrl': {u'LT_innerLower_eyelid_bnd': 0.1,
                               u'LT_inner_eyelid_bnd': 0.1,
                               u'LT_lower_eyelid_bnd': 0.1,
                               u'LT_outerLower_eyelid_bnd': 0.1,
                               u'LT_outer_eyelid_bnd': 0.1},
 u'LT_mid_browA_pri_ctrl': {u'LT_in_browB_bnd': 0.5,
                            u'LT_in_browC_bnd': 0.85,
                            u'LT_mid_browA_bnd': 1.0,
                            u'LT_mid_browB_bnd': 0.85,
                            u'LT_out_browA_bnd': 0.4},
 u'LT_mid_cheek_pri_ctrl': {u'LT__chinA_bnd': 0.15,
                            u'LT__chin_bnd': 0.05,
                            u'LT__sneer_bnd': 0.05,
                            u'LT__squint_bnd': 0.15,
                            u'LT_cornerLow_jaw_bnd': 0.6,
                            u'LT_cornerUp_jaw_bnd': 0.6,
                            u'LT_corner_jaw_bnd': 0.7,
                            u'LT_corner_lip_bnd': 0.3,
                            u'LT_corner_sneer_bnd': 0.25,
                            u'LT_in_cheek_bnd': 0.02,
                            u'LT_lowOut_cheek_bnd': 0.15,
                            u'LT_low_cheek_bnd': 0.25,
                            u'LT_low_crease_bnd': 0.6,
                            u'LT_lowerCorner_lip_bnd': 0.3,
                            u'LT_lowerPinch_lip_bnd': 0.15,
                            u'LT_lowerSneer_lip_bnd': 0.05,
                            u'LT_midCorner_chin_bnd': 0.25,
                            u'LT_midLow_cheek_bnd': 0.7,
                            u'LT_midUp_cheek_bnd': 0.7,
                            u'LT_mid_cheek_bnd': 1.0,
                            u'LT_mid_chin_bnd': 0.05,
                            u'LT_mid_crease_bnd': 0.7,
                            u'LT_out_cheek_bnd': 0.15,
                            u'LT_up_cheek_bnd': 0.05,
                            u'LT_up_crease_bnd': 0.6,
                            u'LT_up_jaw_bnd': 0.15,
                            u'LT_upperCorner_lip_bnd': 0.3,
                            u'LT_upperPinch_lip_bnd': 0.15,
                            u'LT_upperSneer_lip_bnd': 0.05},
 u'LT_out_browB_pri_ctrl': {u'LT_in_browC_bnd': 0.1,
                            u'LT_mid_browA_bnd': 0.2,
                            u'LT_mid_browB_bnd': 0.4,
                            u'LT_out_browA_bnd': 0.75,
                            u'LT_out_browB_bnd': 1.0},
 u'LT_upperSneer_lip_pri_ctrl': {u'CT__sneer_bnd': 0.35,
                                 u'CT_upper_lip_bnd': 0.5,
                                 u'LT__sneer_bnd': 0.5,
                                 u'LT_upperPinch_lip_bnd': 0.5,
                                 u'LT_upperSide_lip_bnd': 0.9,
                                 u'LT_upperSneer_lip_bnd': 1.0,
                                 u'RT_upperSide_lip_bnd': 0.1},
 u'LT_upper_eyelid_pri_ctrl': {u'LT_innerUpper_eyelid_bnd': 0.1,
                               u'LT_inner_eyelid_bnd': 0.1,
                               u'LT_outerUpper_eyelid_bnd': 0.1,
                               u'LT_outer_eyelid_bnd': 0.1,
                               u'LT_upper_eyelid_bnd': 0.1},
 u'RT__browMover_pri_ctrl': {u'CT__brow_bnd': 0.25,
                             u'RT__browMover_bnd': 1.0,
                             u'RT_in_browA_bnd': 0.8,
                             u'RT_in_browB_bnd': 1.0,
                             u'RT_in_browC_bnd': 1.0,
                             u'RT_mid_browA_bnd': 1.0,
                             u'RT_mid_browB_bnd': 0.9,
                             u'RT_out_browA_bnd': 0.8,
                             u'RT_out_browB_bnd': 0.8},
 u'RT__eyeMover_pri_ctrl': {u'CT__brow_bnd': 0.25,
                            u'CT__sneer_bnd': 0.25,
                            u'CT_low_eyeSocket_bnd': 0.25,
                            u'CT_mid_eyeSocket_bnd': 0.25,
                            u'CT_up_eyeSocket_bnd': 0.25,
                            u'RT__eyeMover_bnd': 1.0,
                            u'RT__sneer_bnd': 0.25,
                            u'RT__squint_bnd': 0.25,
                            u'RT_corner_sneer_bnd': 0.25,
                            u'RT_inCorner_eyeSocket_bnd': 1.0,
                            u'RT_in_cheek_bnd': 1.0,
                            u'RT_in_eyeSocket_bnd': 1.0,
                            u'RT_innerLower_eyelid_bnd': 1.0,
                            u'RT_innerUpper_eyelid_bnd': 1.0,
                            u'RT_inner_eyelid_bnd': 1.0,
                            u'RT_lower_eyelid_bnd': 1.0,
                            u'RT_midUp_cheek_bnd': 0.25,
                            u'RT_mid_eyeSocket_bnd': 1.0,
                            u'RT_outCorner_eyeSocket_bnd': 1.0,
                            u'RT_out_cheek_bnd': 1.0,
                            u'RT_out_eyeSocket_bnd': 1.0,
                            u'RT_outerLower_eyelid_bnd': 1.0,
                            u'RT_outerUpper_eyelid_bnd': 1.0,
                            u'RT_outer_eyelid_bnd': 1.0,
                            u'RT_up_cheek_bnd': 1.0,
                            u'RT_up_crease_bnd': 0.25,
                            u'RT_up_squint_bnd': 0.25,
                            u'RT_upper_eyelid_bnd': 1.0},
 u'RT__squint_pri_ctrl': {u'RT__sneer_bnd': 0.05,
                          u'RT__squint_bnd': 1.0,
                          u'RT_cornerLow_jaw_bnd': 0.05,
                          u'RT_cornerUp_jaw_bnd': 0.25,
                          u'RT_corner_jaw_bnd': 0.15,
                          u'RT_corner_sneer_bnd': 0.25,
                          u'RT_in_cheek_bnd': 0.25,
                          u'RT_low_crease_bnd': 0.05,
                          u'RT_midLow_cheek_bnd': 0.05,
                          u'RT_midUp_cheek_bnd': 0.5,
                          u'RT_mid_cheek_bnd': 0.15,
                          u'RT_mid_crease_bnd': 0.15,
                          u'RT_out_cheek_bnd': 0.85,
                          u'RT_up_cheek_bnd': 0.5,
                          u'RT_up_crease_bnd': 0.5,
                          u'RT_up_jaw_bnd': 0.3},
 u'RT_corner_lip_pri_ctrl': {u'CT__chin_bnd': 0.05,
                             u'CT__sneer_bnd': 0.1,
                             u'CT_lower_lip_bnd': 0.1,
                             u'CT_mid_chin_bnd': 0.1,
                             u'CT_upper_lip_bnd': 0.1,
                             u'RT__chinA_bnd': 0.175,
                             u'RT__chin_bnd': 0.25,
                             u'RT__sneer_bnd': 0.4,
                             u'RT_cornerLow_jaw_bnd': 0.075,
                             u'RT_cornerUp_jaw_bnd': 0.075,
                             u'RT_corner_jaw_bnd': 0.075,
                             u'RT_corner_lip_bnd': 1.0,
                             u'RT_corner_sneer_bnd': 0.8,
                             u'RT_in_chin_bnd': 0.15,
                             u'RT_in_forehead_bnd': 0.5,
                             u'RT_lowOut_cheek_bnd': 0.05,
                             u'RT_low_cheek_bnd': 0.15,
                             u'RT_low_crease_bnd': 0.65,
                             u'RT_lowerCorner_lip_bnd': 0.98,
                             u'RT_lowerPinch_lip_bnd': 0.785,
                             u'RT_lowerSide_lip_bnd': 0.3,
                             u'RT_lowerSneer_lip_bnd': 0.53,
                             u'RT_midCorner_chin_bnd': 0.85,
                             u'RT_midLow_cheek_bnd': 0.4,
                             u'RT_midUp_cheek_bnd': 0.4,
                             u'RT_mid_cheek_bnd': 0.52,
                             u'RT_mid_chin_bnd': 0.45,
                             u'RT_mid_crease_bnd': 0.75,
                             u'RT_up_crease_bnd': 0.6,
                             u'RT_upperCorner_lip_bnd': 0.98,
                             u'RT_upperPinch_lip_bnd': 0.785,
                             u'RT_upperSide_lip_bnd': 0.3,
                             u'RT_upperSneer_lip_bnd': 0.53},
 u'RT_in_browA_pri_ctrl': {u'CT__brow_bnd': 0.5,
                           u'RT_in_browA_bnd': 1.0,
                           u'RT_in_browB_bnd': 0.65,
                           u'RT_in_browC_bnd': 0.4,
                           u'RT_mid_browA_bnd': 0.15},
 u'RT_lowerSneer_lip_pri_ctrl': {u'CT_lower_lip_bnd': 0.5,
                                 u'CT_mid_chin_bnd': 0.35,
                                 u'LT_lowerSide_lip_bnd': 0.1,
                                 u'RT_lowerPinch_lip_bnd': 0.5,
                                 u'RT_lowerSide_lip_bnd': 0.9,
                                 u'RT_lowerSneer_lip_bnd': 1.0,
                                 u'RT_mid_chin_bnd': 0.5},
 u'RT_lower_eyelid_pri_ctrl': {u'RT_innerLower_eyelid_bnd': 0.1,
                               u'RT_inner_eyelid_bnd': 0.1,
                               u'RT_lower_eyelid_bnd': 0.1,
                               u'RT_outerLower_eyelid_bnd': 0.1,
                               u'RT_outer_eyelid_bnd': 0.1},
 u'RT_mid_browA_pri_ctrl': {u'RT_in_browB_bnd': 0.5,
                            u'RT_in_browC_bnd': 0.85,
                            u'RT_mid_browA_bnd': 1.0,
                            u'RT_mid_browB_bnd': 0.85,
                            u'RT_out_browA_bnd': 0.4},
 u'RT_mid_cheek_pri_ctrl': {u'RT__chinA_bnd': 0.15,
                            u'RT__chin_bnd': 0.05,
                            u'RT__sneer_bnd': 0.05,
                            u'RT__squint_bnd': 0.15,
                            u'RT_cornerLow_jaw_bnd': 0.6,
                            u'RT_cornerUp_jaw_bnd': 0.6,
                            u'RT_corner_jaw_bnd': 0.7,
                            u'RT_corner_lip_bnd': 0.3,
                            u'RT_corner_sneer_bnd': 0.25,
                            u'RT_in_cheek_bnd': 0.02,
                            u'RT_lowOut_cheek_bnd': 0.15,
                            u'RT_low_cheek_bnd': 0.25,
                            u'RT_low_crease_bnd': 0.6,
                            u'RT_lowerCorner_lip_bnd': 0.3,
                            u'RT_lowerPinch_lip_bnd': 0.15,
                            u'RT_lowerSneer_lip_bnd': 0.05,
                            u'RT_midCorner_chin_bnd': 0.25,
                            u'RT_midLow_cheek_bnd': 0.7,
                            u'RT_midUp_cheek_bnd': 0.7,
                            u'RT_mid_cheek_bnd': 1.0,
                            u'RT_mid_chin_bnd': 0.05,
                            u'RT_mid_crease_bnd': 0.7,
                            u'RT_out_cheek_bnd': 0.15,
                            u'RT_up_cheek_bnd': 0.05,
                            u'RT_up_crease_bnd': 0.6,
                            u'RT_up_jaw_bnd': 0.15,
                            u'RT_upperCorner_lip_bnd': 0.3,
                            u'RT_upperPinch_lip_bnd': 0.15,
                            u'RT_upperSneer_lip_bnd': 0.05},
 u'RT_out_browB_pri_ctrl': {u'RT_in_browC_bnd': 0.1,
                            u'RT_mid_browA_bnd': 0.2,
                            u'RT_mid_browB_bnd': 0.4,
                            u'RT_out_browA_bnd': 0.75,
                            u'RT_out_browB_bnd': 1.0},
 u'RT_upperSneer_lip_pri_ctrl': {u'CT__sneer_bnd': 0.35,
                                 u'CT_upper_lip_bnd': 0.5,
                                 u'LT_upperSide_lip_bnd': 0.1,
                                 u'RT__sneer_bnd': 0.5,
                                 u'RT_upperPinch_lip_bnd': 0.5,
                                 u'RT_upperSide_lip_bnd': 0.9,
                                 u'RT_upperSneer_lip_bnd': 1.0},
 u'RT_upper_eyelid_pri_ctrl': {u'RT_innerUpper_eyelid_bnd': 0.1,
                               u'RT_inner_eyelid_bnd': 0.1,
                               u'RT_outerUpper_eyelid_bnd': 0.1,
                               u'RT_outer_eyelid_bnd': 0.1,
                               u'RT_upper_eyelid_bnd': 0.1}}
