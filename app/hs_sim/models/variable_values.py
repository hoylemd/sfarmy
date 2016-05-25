def direct_damage_value(amount=0):
    return 1.5 * amount


def spell_damage(amount=1):
    return amount

mapping = {
    'direct_damage': direct_damage_value,
    'spell_damage': spell_damage
}
