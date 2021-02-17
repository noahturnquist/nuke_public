#-------------------------------------------------------------------
#	menu.py
#	Version: 1.0.1
#	Last Updated: February 17th 2021
#-------------------------------------------------------------------
#
#-------------------------------------------------------------------


#-------------------------------------------------------------------
#	GLOBAL IMPORTS	::::::::::::::::::::::::::::::::::::::::::::::::
#-------------------------------------------------------------------

import nuke
import platform
import nukescripts


#-------------------------------------------------------------------
#	DIRECTORIES	::::::::::::::::::::::::::::::::::::::::::::::::
#-------------------------------------------------------------------

main_dir = 'C:/Users/noah.turnquist/.nuke/'
icon_dir = 'C:/Users/noah.turnquist/.nuke/icons/'

#-------------------------------------------------------------------
#	GIZMOS	::::::::::::::::::::::::::::::::::::::::::::::::
#-------------------------------------------------------------------


#SPIN VFX GIZMOS
spinvfxMenu = nuke.menu('Nodes').addMenu('spinvfx', icon = icon_dir + 'spin_vfx_icon.png')

spinvfxMenu.addCommand('Edge_Expand', 'nuke.createNode("edge_expand")')
spinvfxMenu.addCommand('Erode_Fine', 'nuke.createNode("erode_fine")')


#NUKEPEDIA GIZMOS
nukepedia_menu = nuke.menu('Nodes').addMenu('nukepedia', icon = icon_dir + 'nukepedia_icon.png')

nukepedia_menu.addCommand('Gradient_Magic', 'nuke.createNode("gradient_magic")')
nukepedia_menu.addCommand('L_Grain', 'nuke.createNode("l_grain")')



#-------------------------------------------------------------------
#	COMMANDS	::::::::::::::::::::::::::::::::::::::::::::::::
#-------------------------------------------------------------------

utilities_menu = nuke.menu('Nuke').addMenu('Utilities')

utilities_menu.addCommand('Autocrop', 'nukescripts.autocrop()')


import relative_cornerpins
utilities_menu.addCommand('Relative_Cornerpin', 'relative_cornerpins.relative_cornerpins()')

import backdrops_setter
utilities_menu.addCommand('Backdrops_Setter', 'backdrops_setter.backdrop_setter()')



#-------------------------------------------------------------------
#	KNOB DEFAULTS	::::::::::::::::::::::::::::::::::::::::::::::::
#-------------------------------------------------------------------

#2D Tracker Defaults
nuke.knobDefault('Tracker4.shutteroffset', "centered")
nuke.knobDefault('Tracker4.label', "Motion: [value transform]\nRef: [value reference_frame]")

nuke.addOnUserCreate(lambda:nuke.thisNode()['reference_frame'].setValue(nuke.frame()), nodeClass='Tracker4')


#Framehold Defaults
nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass='FrameHold')


# ----- Center Shutter ---------------------------
nuke.knobDefault('Tracker4.shutteroffset', "centered")
nuke.knobDefault('TimeBlur.shutteroffset', "centered")
nuke.knobDefault('Transform.shutteroffset', "centered")
nuke.knobDefault('TransformMasked.shutteroffset', "centered")
nuke.knobDefault('CornerPin2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur3D.shutteroffset', "centered")
nuke.knobDefault('ScanlineRender.shutteroffset', "centered")
nuke.knobDefault('Card3D.shutteroffset', "centered")



#-------------------------------------------------------------------
#	KEYBOARD SHORTCUTS	::::::::::::::::::::::::::::::::::::::::::::
#-------------------------------------------------------------------

#TRACKER
nuke.menu('Nodes').addCommand("Transform/Tracker", "nuke.createNode('Tracker4')", "ctrl+alt+t", icon="Tracker.png", shortcutContext = 2)


#---------- Merge Shortcuts ----------------------------

mergeMenu = nuke.menu('Nodes').findItem("Merge/Merges")

mergeMenu.addCommand('Stencil', 'nuke.createNode("Merge2", "operation stencil bbox B")', "alt+o", icon="Out.png", shortcutContext = 2)
mergeMenu.addCommand('Mask', 'nuke.createNode("Merge2", "operation mask bbox A")', "alt+i", icon="Out.png", shortcutContext = 2)
mergeMenu.addCommand('Plus', 'nuke.createNode("Merge2", "operation plus")', "alt+]", icon="Out.png", shortcutContext = 2)
mergeMenu.addCommand('From', 'nuke.createNode("Merge2", "operation from bbox B")', "alt+[", icon="Out.png", shortcutContext = 2)
