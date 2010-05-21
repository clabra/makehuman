#
#	Panel bone definitions
#

import mhx_rig
from mhx_rig import *

offs = [0, 0, 0.3]

PanelJoints = [
	('origin',		'o', ('head', [-3.3, 0.5, 0.0])),
	('PFace',		'o', ('origin', [0.0, -1.5, 0.0])),
	('PBrow_R',		'o', ('origin', [-0.4, 0.8, 0.0])),
	('PBrow_L',		'o', ('origin', [0.4, 0.8, 0.0])),
	('PBrows',		'o', ('origin', [0.0, 0.8, 0.0])),
	('PUpLid_R',		'o', ('origin', [-0.4, 0.6, 0.0])),
	('PUpLid_L',		'o', ('origin', [0.4, 0.6, 0.0])),
	('PLoLid_R',		'o', ('origin', [-0.4, 0.2, 0.0])),
	('PLoLid_L',		'o', ('origin', [0.4, 0.2, 0.0])),
	('PCheek_R',		'o', ('origin', [-0.4, 0.0, 0.0])),
	('PCheek_L',		'o', ('origin', [0.4, 0.0, 0.0])),
	('PUpLip',		'o', ('origin', [0.0, -0.2, 0.0])),
	('PLoLip',		'o', ('origin', [0.0, -0.8, 0.0])),
	('PMouth',		'o', ('origin', [0.0, -0.5, 0.0])),
	('PUpLip_R',		'o', ('origin', [-0.2, -0.4, 0.0])),
	('PUpLip_L',		'o', ('origin', [0.2, -0.4, 0.0])),
	('PLoLip_R',		'o', ('origin', [-0.2, -0.6, 0.0])),
	('PLoLip_L',		'o', ('origin', [0.2, -0.6, 0.0])),
	('PMouth_R',		'o', ('origin', [-0.5, -0.5, 0.0])),
	('PMouth_L',		'o', ('origin', [0.5, -0.5, 0.0])),
	('PTounge',		'o', ('origin', [0.0, -1.0, 0.0])),
	('PJaw',		'o', ('origin', [0.0, -1.1, 0.0])),

	('PArmIK_R',		'o', ('origin', [-1.1, 2.0, 0.0])),
	('PArmIK_L',		'o', ('origin', [0.1, 2.0, 0.0])),
	('PLegIK_R',		'o', ('origin', [-1.1, 1.5, 0.0])),
	('PLegIK_L',		'o', ('origin', [0.1, 1.5, 0.0])),

	('PHandLocal_R',	'o', ('origin', [-1.1, 2.0, 0.0])),
	('PHandLocal_L',	'o', ('origin', [0.1, 2.0, 0.0])),
	('PFootLocal_R',	'o', ('origin', [-1.1, 1.5, 0.0])),
	('PFootLocal_L',	'o', ('origin', [0.1, 1.5, 0.0])),

	('MHRelax_L',		'o', ('origin', [1.5, 1.0, 0.0])),
	('MHCurl_L',		'o', ('MHRelax_L', [0.0, -0.5, 0.0])),
	('MHCone_L',		'o', ('MHRelax_L', [0.0, -1.0, 0.0])),
	('MHSpread_L',		'o', ('MHRelax_L', [0.0, -1.5, 0.0])),
	('MHScrunch_L',		'o', ('MHRelax_L', [0.0, -2.0, 0.0])),
	('MHLean_L',		'o', ('MHRelax_L', [0.0, -2.5, 0.0])),

	('MHRelax_R',		'o', ('origin', [-1.5, 1.0, 0.0])),
	('MHCurl_R',		'o', ('MHRelax_R', [0.0, -0.5, 0.0])),
	('MHCone_R',		'o', ('MHRelax_R', [0.0, -1.0, 0.0])),
	('MHSpread_R',		'o', ('MHRelax_R', [0.0, -1.5, 0.0])),
	('MHScrunch_R',		'o', ('MHRelax_R', [0.0, -2.0, 0.0])),
	('MHLean_R',		'o', ('MHRelax_R', [0.0, -2.5, 0.0])),

]

PanelHeadsTails = [
	('PFace',			'PFace', ('PFace', [0,0,-1])),
	('PFaceDisp',			'origin', ('origin', [0,0,-1])),
	('PBrow_R',			'PBrow_R', ('PBrow_R', offs)),
	('PBrow_L',			'PBrow_L', ('PBrow_L', offs)),
	('PBrows',			'PBrows', ('PBrows', offs)),
	('PUpLid_R',			'PUpLid_R', ('PUpLid_R', offs)),
	('PUpLid_L',			'PUpLid_L', ('PUpLid_L', offs)),
	('PLoLid_R',			'PLoLid_R', ('PLoLid_R', offs)),
	('PLoLid_L',			'PLoLid_L', ('PLoLid_L', offs)),
	('PCheek_R',			'PCheek_R', ('PCheek_R', offs)),
	('PCheek_L',			'PCheek_L', ('PCheek_L', offs)),
	('PNose',			'origin', ('origin', offs)),
	#('PUpLip',			'PUpLip', ('PUpLip', offs)),
	#('PLoLip',			'PLoLip', ('PLoLip', offs)),
	#('PMouth',			'PMouth', ('PMouth', offs)),
	('PUpLip_R',			'PUpLip_R', ('PUpLip_R', offs)),
	('PUpLip_L',			'PUpLip_L', ('PUpLip_L', offs)),
	('PLoLip_R',			'PLoLip_R', ('PLoLip_R', offs)),
	('PLoLip_L',			'PLoLip_L', ('PLoLip_L', offs)),
	('PMouth_R',			'PMouth_R', ('PMouth_R', offs)),
	('PMouth_L',			'PMouth_L', ('PMouth_L', offs)),
	('PTounge',			'PTounge', ('PTounge', offs)),
	('PJaw',			'PJaw', ('PJaw', offs)),

	('PArmIK_R',			'PArmIK_R', ('PArmIK_R', offs)),
	('PArmIK_L',			'PArmIK_L', ('PArmIK_L', offs)),
	('PLegIK_R',			'PLegIK_R', ('PLegIK_R', offs)),
	('PLegIK_L',			'PLegIK_L', ('PLegIK_L', offs)),
	#('PHandLocal_R',		'PHandLocal_R', ('PHandLocal_R', offs)),
	#('PHandLocal_L',		'PHandLocal_L', ('PHandLocal_L', offs)),
	#('PFootLocal_R',		'PFootLocal_R', ('PFootLocal_R', offs)),
	#('PFootLocal_L',		'PFootLocal_L', ('PFootLocal_L', offs)),

	('MHRelax_L',			'MHRelax_L', ('MHRelax_L', offs)),
	('MHCurl_L',			'MHCurl_L', ('MHCurl_L', offs)),
	('MHCone_L',			'MHCone_L', ('MHCone_L', offs)),
	('MHSpread_L',			'MHSpread_L', ('MHSpread_L', offs)),
	('MHScrunch_L',			'MHScrunch_L', ('MHScrunch_L', offs)),
	('MHLean_L',			'MHLean_L', ('MHLean_L', offs)),

	('MHRelax_R',			'MHRelax_R', ('MHRelax_R', offs)),
	('MHCurl_R',			'MHCurl_R', ('MHCurl_R', offs)),
	('MHCone_R',			'MHCone_R', ('MHCone_R', offs)),
	('MHSpread_R',			'MHSpread_R', ('MHSpread_R', offs)),
	('MHScrunch_R',			'MHScrunch_R', ('MHScrunch_R', offs)),
	('MHLean_R',			'MHLean_R', ('MHLean_R', offs)),
	]


PanelArmature = [
	('PFace', T_Panel,		pi, None, F_WIR, L_PANEL, (1,1,1) ),
	('PFaceDisp', T_Panel,		pi, 'PFace', F_WIR+F_RES, L_PANEL, (1,1,1) ),
	('PBrow_R', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('PBrow_L', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('PBrows', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('PUpLid_R', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('PUpLid_L', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('PLoLid_R', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('PLoLid_L', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('PCheek_R', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('PCheek_L', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('PNose', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	#('PUpLip', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	#('PLoLip', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	#('PMouth', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('PUpLip_R', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('PUpLip_L', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('PLoLip_R', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('PLoLip_L', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('PMouth_R', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('PMouth_L', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('PTounge', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('PJaw', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),

	('PArmIK_R', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('PArmIK_L', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('PLegIK_R', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('PLegIK_L', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	#('PHandLocal_R', T_Panel,	pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	#('PHandLocal_L', T_Panel,	pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	#('PFootLocal_R', T_Panel,	pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	#('PFootLocal_L', T_Panel,	pi, 'PFace', 0, L_PANEL, (1,1,1) ),

	('MHRelax_L', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('MHCurl_L', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('MHCone_L', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('MHSpread_L', T_Panel,	pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('MHScrunch_L', T_Panel,	pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('MHLean_L', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),

	('MHRelax_R', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('MHCurl_R', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('MHCone_R', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('MHSpread_R', T_Panel,	pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('MHScrunch_R', T_Panel,	pi, 'PFace', 0, L_PANEL, (1,1,1) ),
	('MHLean_R', T_Panel,		pi, 'PFace', 0, L_PANEL, (1,1,1) ),

]

#
#	PanelWritePoses(fp):
#

MX = 0.25


PanelPoses = [
	('poseBone', T_Panel, 'PFace', 'MHCube05', None, (0,0,0), (0,0,0), (0,0,0), (1,1,1), 0, []),

	('poseBone', T_Panel, 'PFaceDisp', 'MHFace', None, (1,1,1), (1,1,1), (1,1,1), (1,1,1), 0, []),

	('cSlider',  'PBrow_L', MX),
	('cSlider',  'PBrow_R', MX),
	('cSlider',  'PBrows', MX),
	('cSlider',  'PUpLid_L', MX),
	('cSlider',  'PUpLid_R', MX),
	('cSlider',  'PLoLid_L', MX),
	('cSlider',  'PLoLid_R', MX),
	('cSlider',  'PCheek_L', MX),
	('cSlider',  'PCheek_R', MX),
	('cSlider',  'PNose', MX),
	('cSlider',  'PUpLip_L', MX),
	('cSlider',  'PUpLip_R', MX),
	('cSlider',  'PLoLip_L', MX),
	('cSlider',  'PLoLip_R', MX),
	('cSlider',  'PMouth_L', MX),
	('cSlider',  'PMouth_R', MX),
	('cSlider',  'PTounge', MX),
	('cSlider',  'PJaw', MX),

	('xSlider', 'PArmIK_L', 0.0, 1.0),
	('xSlider', 'PArmIK_R', 0.0, 1.0),
	('xSlider', 'PLegIK_L', 0.0, 1.0),
	('xSlider', 'PLegIK_R', 0.0, 1.0),
	#('xSlider', 'PHandLocal_L', 0.0, 1.0),
	#('xSlider', 'PHandLocal_R', 0.0, 1.0),
	#('xSlider', 'PFootLocal_L', 0.0, 1.0),
	#('xSlider', 'PFootLocal_R', 0.0, 1.0),

	('xSlider', 'MHRelax_L', -0.25, 0.5),
	('xSlider', 'MHCurl_L', -0.25, 0.5),
	('xSlider', 'MHCone_L', -0.25, 0.5),
	('xSlider', 'MHSpread_L', -0.25, 0.5),
	('xSlider', 'MHScrunch_L', -0.25, 0.5),
	('xSlider', 'MHLean_L', -0.5, 0.5),

	('xSlider', 'MHRelax_R', -0.5, 0.25),
	('xSlider', 'MHCurl_R', -0.5, 0.25),
	('xSlider', 'MHCone_R', -0.5, 0.25),
	('xSlider', 'MHSpread_R', -0.5, 0.25),
	('xSlider', 'MHScrunch_R', -0.5, 0.25),
	('xSlider', 'MHLean_R', -0.5, 0.5),
]

'''
	'BendElbowForward_L' : ('LoArm_L', 'ROT_X', 1, 0, 1)],
	'BendElbowForward_R' : ('LoArm_R', 'ROT_X', 1, 0, 1)],
	'BendHeadForward' : ('Head', 'ROT_X', 3, 0, 1)],
	'BendKneeBack_L' : ('LoLeg_L', 'ROT_X', -2, -1, 0)],
	'BendKneeBack_R' : ('LoLeg_R', 'ROT_X', -2, -1, 0)],
	'BendLegBack_L' : ('UpLeg_L'), 'ROT_X', -1, -1, 0)],
	'BendLegBack_R' : ('UpLeg_R', 'ROT_X', -1, -1, 0)],
	'BendLegForward_L' : ('UpLeg_L', 'ROT_X', 1, 0, 1)],
	'BendLegForward_R' : ('UpLeg_R', 'ROT_X', 1, 0, 1)],
	'ShoulderDown_L' : ('UpArm_L', 'ROT_Z', 1, -1, 0)],
	'ShoulderDown_R' : ('UpArm_R', 'ROT_Z', 1, 0, 1)],
'''
#
#	Face representation
#

K = 1.0/MX

FaceDrivers = {
	# Brows
	'BrowsMidDown' : ('PBrows', 'LOC_Z', (0,K)),
	'BrowsMidUp' : ('PBrows', 'LOC_Z', (0,-K)),
	'BrowsSqueeze' : ('PBrows', 'LOC_X', (0,-K)),
	'BrowsDown_L' : ('PBrow_L', 'LOC_Z', (0,K)),
	'BrowsDown_R' : ('PBrow_R', 'LOC_Z', (0,K)),
	'BrowsOutUp_L' : ('PBrow_L', 'LOC_Z', (0,-K)),
	'BrowsOutUp_R' : ('PBrow_R', 'LOC_Z', (0,-K)),

#	Lids
	#'UpLidDown_L' : ('PUpLid_L', 'LOC_Z', (0,K)),
	#'UpLidDown_R' : ('PUpLid_R', 'LOC_Z', (0,K)),
	#'LoLidUp_L' : ('PLoLid_L', 'LOC_Z', (0,-K)),
	#'LoLidUp_R' : ('PLoLid_R', 'LOC_Z', (0,-K)),

#	Nose and jaw

	'Sneer_L' : ('PNose', 'LOC_X', (0,K)), 
	'Sneer_R' : ('PNose', 'LOC_X', (0,-K)), 
	'CheekUp_L' : ('PCheek_L', 'LOC_Z', (0,-K)),
	'CheekUp_R' : ('PCheek_R', 'LOC_Z', (0,-K)),
	'Squint_L' : ('PCheek_L', 'LOC_X', (0,K)),
	'Squint_R' : ('PCheek_R', 'LOC_X', (0,-K)),

#	Jaw and tounge
	'MouthOpen' : ('PJaw', 'LOC_Z', (0,K)),
	'TongueOut' : ('PJaw', 'LOC_X', (0,-K)),
	'ToungeUp' : ('PTounge', 'LOC_Z', (0,-K)),
	'ToungeLeft' : ('PTounge', 'LOC_X', (0,K)),
	'ToungeRight' : ('PTounge', 'LOC_X', (0,-K)),

#	Mouth expressions
	'Smile_L' : ('PMouth_L', 'LOC_X', (0,K)),
	'Smile_R' : ('PMouth_R', 'LOC_X', (0,-K)),
	'Frown_L' : ('PMouth_L', 'LOC_Z', (0,K)),
	'Frown_R' : ('PMouth_R', 'LOC_Z', (0,K)), 
	'Narrow_L' : ('PMouth_L', 'LOC_X', (0,-K)), 
	'Narrow_R' : ('PMouth_R', 'LOC_X', (0,K)),

#	Lips
	'UpLipUp_L' : ('PUpLip_L', 'LOC_Z', (0,-K)), 
	'UpLipUp_R' : ('PUpLip_R', 'LOC_Z', (0,-K)), 
	'UpLipDown_L' : ('PUpLip_L', 'LOC_Z', (0,K)), 
	'UpLipDown_R' : ('PUpLip_R', 'LOC_Z', (0,K)), 
	'LoLipUp_L' : ('PLoLip_L', 'LOC_Z', (0,-K)), 
	'LoLipUp_R' : ('PLoLip_R', 'LOC_Z', (0,-K)), 
	'LoLipDown_L' : ('PLoLip_L', 'LOC_Z', (0,K)), 
	'LoLipDown_R' : ('PLoLip_R', 'LOC_Z', (0,K)), 
}

