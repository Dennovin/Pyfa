# Used by:
# Variations of ship: Hurricane (2 of 2)
# Ship: Claymore
# Ship: Sleipnir
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Minmatar Battlecruiser").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Projectile Turret"),
                                  "speed", ship.getModifiedItemAttr("shipBonusMBC2") * level)
