define xRotAnchor = 0
define yRotAnchor = 0.5

#ZOOMINGIN
define zoomRate = 0.3
#region Entering
transform zoomInHalftLeft:
    xpos -0.5
    ypos 1.0
    easein zoomRate SlightLeft
    easeout zoomRate HalfLeft

transform zoomInLeft:
    xpos -0.5
    ypos 1.0
    easein zoomRate SlightLeftMore
    easeout zoomRate LeftSide

transform zoomInHalfRight:
    xpos -0.5
    ypos 1.0
    easein zoomRate HalfRight

transform zoomInRight:
    xpos -0.5
    ypos 1.0
    easein zoomRate RightSide

#endregion
#ZOOMINGIN 


#ANCHORS
#region Anchors
transform AnchorZero:
    xanchor 0.0
    yanchor 0.0

transform AnchorHalf:
    xanchor 0.5
    yanchor 0.5

transform AnchorHalfTop:
    xanchor 0.5
    yanchor 0.0

transform AnchorHalfBottom:
    xanchor 0.5
    yanchor 1.0

transform AnchorOne:
    xanchor 1.0
    yanchor 1.0
#endregion
#ANCHORS


#MOVERS
#region Movers
transform MoveToLeft:
    easein zoomRate LeftSide

transform MoveToHalfLeft:
    easein zoomRate HalfLeft

transform MoveToSlightLeft:
    easein zoomRate SlightLeft

transform MoveToRight:
    easein zoomRate RightSide

transform MoveToRightish:
    easein zoomRate MiddleRight

transform MoveToHalfRight:
    easein zoomRate HalfRight

transform MoveToMiddle:
    easein zoomRate middle
#endregion
#MOVERS

define cutInrate = 0.5

transform CutIn:
    yalign 0.8 xalign 0.5 alpha 0.5
    easein cutInrate yalign 0.5 alpha 1.0

transform CutOut:
    easein cutInrate yalign 0.2 alpha 0.0

#PROXIMITY
#region Proximity
transform Close:
    zoom 2.0
    offset (0, 250)

transform VeryClose:
    zoom 3.0
    offset (0, 100)
#endregion
#PROXIMITY

#FLIPPERS
define flipRate = 0.2
#region Flippers

transform flipLeft:
    transform_anchor True  
    linear flipRate xzoom -1.0 yzoom 1.0
    offset (0, 0)

transform flipRight:
    transform_anchor True  
    linear flipRate xzoom 1.0 yzoom 1.0
    offset (0, 0)

transform Normalize:
    zoom 1.0
    offset (0, 0)
#endregion
#FLIPPERS

#EXIT
define exitRate = 1.1
transform exitLeft:
    easeout_expo exitRate xpos -1.0

transform exitRight:
    easeout_expo exitRate xpos 1.0

#EXIT




#Smaller number = faster easing
#Larger number = slower easing
define jumpRate = 0.2
define jumpHeight = -50 #offset is reversed, negative is up and postiive is down
define jumpHeightLow = 50

define shakeMultiplier = 0.8
define shakeRate = 0.05

define proudRate = 0.4

define sadDropRate = 0.5
define sadLowDistance = 51

define confuseRotateRate = 0.3
define confuseAngle = 10

#EMOTES
#region Emotes



transform spookedAnim:
    linear 0.04 xzoom 0.95 yzoom 0.95 offset(0, 60)
    linear 0.06 xzoom 0.85 yzoom 1.35 offset(0, -10)
    linear 0.05 xzoom 1.1 yzoom 0.95 offset(0, 70)
    easein 0.12 xzoom 1.0 yzoom 1.0 offset(0, 0)


transform scaredAnim:
    linear shakeRate xoffset 2 * shakeMultiplier yoffset -6 * shakeMultiplier
    linear shakeRate xoffset -2.8 * shakeMultiplier yoffset -2 * shakeMultiplier
    linear shakeRate xoffset 2.8 * shakeMultiplier yoffset -2 * shakeMultiplier
    linear shakeRate xoffset -2 * shakeMultiplier yoffset -6 * shakeMultiplier
    linear shakeRate xoffset +0 yoffset +0
    repeat

transform jumpAnim:
    easein jumpRate offset (0.0, jumpHeight)
    easeout jumpRate offset (0.0, jumpHeightLow)
    easein jumpRate offset (0.0, jumpHeight)
    easeout jumpRate offset (0.0, 0.0)

transform jumpLoopAnim:
    easein jumpRate offset (0.0, jumpHeight)
    easeout jumpRate offset (0.0, jumpHeightLow)
    easein jumpRate offset (0.0, jumpHeight)
    easeout jumpRate offset (0.0, jumpHeightLow)
    repeat

transform happyAnim:
    linear 0.2 xzoom 1.05 yzoom 1.05
    linear 0.2 xzoom 1.05 yzoom 0.9
    linear 0.2 xzoom 0.95 yzoom 1.1
    linear 0.2 xzoom 1.05 yzoom 0.95
    linear 0.2 xzoom 1.00 yzoom 1.00


transform sadAnim:
    easein sadDropRate offset (0, sadLowDistance)


transform proudAnim:
    easein 0.2 zoom 0.95
    easein proudRate zoom 1.05
    easeout proudRate + 0.1 zoom 1.0


transform confuseFacingRight:
    transform_anchor True      
    easein confuseRotateRate rotate confuseAngle
    

transform confuseFacingLeft:
    transform_anchor True   
    easein confuseRotateRate rotate -confuseAngle

#endregion
#EMOTES


transform ResetOffset:
    offset (0, 0)



transform Straighten:
    transform_anchor True
    easein confuseRotateRate rotate 0

transform FastStraighten:
    transform_anchor True
    rotate 0


#region Positions


transform TopLeft:
    xpos 0.0
    ypos 0.0

transform LeftSide:
    xpos 0.1
    ypos 0.0

transform SlightLeft:
    xpos 0.15
    ypos 0.0

transform HalfLeft:
    xpos 0.25
    ypos 0.0

transform MiddleLeft:
    xpos 0.4
    ypos 0.0

transform SlightLeftMore:
    xpos 0.3
    ypos 0.0

transform HalfRight:
    xpos 0.75
    ypos 0.0

transform RightSide:
    xpos 0.9
    ypos 0.0

transform Quarter:
    xpos 0.25
    ypos 0.25

transform Center:
    xpos 0.5
    ypos 0.5

transform topmiddle:
    xpos 0.5
    ypos 0.0

transform MiddleRight:
    xpos 0.6
    ypos 0.0

transform middle:
    xpos 0.5
    ypos 0.0

transform slightUp:
    ypos 0.4

#endregion







#region Shaders

transform TintShader:
    matrixcolor TintMatrix("#434343")

transform NormalTint:
    matrixcolor TintMatrix("#ffffff")

transform HueShader:
    matrixcolor HueMatrix(-150)

transform BrightnessShader:
    matrixcolor BrightnessMatrix(-0.25)


    
transform NormalBrightness:
    matrixcolor BrightnessMatrix(0.0)

#endregion