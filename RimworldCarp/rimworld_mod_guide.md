# RimWorld Mod: Carpentry & Wooden Planks

This mod adds a carpentry system to RimWorld, allowing you to process wood into planks and build plank walls. Here's the complete file structure and code:

## File Structure
```
CarpentryMod/
├── About/
│   ├── About.xml
│   └── Preview.png (512x512 image for Steam Workshop)
├── Defs/
│   ├── ThingDefs_Buildings/
│   │   ├── Buildings_Production.xml
│   │   └── Buildings_Structure.xml
│   ├── ThingDefs_Items/
│   │   └── Items_Resource.xml
│   └── RecipeDefs/
│       └── Recipes_Carpentry.xml
├── Textures/
│   └── Things/
│       ├── Building/
│       │   ├── Production/
│       │   │   └── CarpentryBench.png (64x64)
│       │   └── Linked/
│       │       └── PlankWall_Atlas.png (64x192)
│       └── Item/
│           └── Resource/
│               └── WoodenPlanks.png (64x64)
└── Languages/
    └── English/
        └── Keyed/
            └── Keys.xml
```

## About/About.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<ModMetaData>
    <n>Carpentry &amp; Wooden Planks</n>
    <author>YourName</author>
    <supportedVersions>
        <li>1.4</li>
        <li>1.5</li>
    </supportedVersions>
    <modDependencies>
    </modDependencies>
    <loadAfter>
    </loadAfter>
    <description>Adds a carpentry system to RimWorld! Process raw wood into refined wooden planks and build beautiful plank walls.

Features:
- Carpentry Bench: Process wood into wooden planks (2 wood → 1 plank)
- Wooden Planks: A refined building material
- Plank Walls: Attractive walls made from 3 wooden planks
- Unlocked with Smithing research

Perfect for colonies that want to make better use of their abundant wood resources while creating more refined structures.</description>
    <packageId>yourname.carpentry</packageId>
    <url>https://github.com/yourusername/rimworld-carpentry</url>
</ModMetaData>
```

## Defs/ThingDefs_Items/Items_Resource.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<Defs>
    <ThingDef ParentName="ResourceBase">
        <defName>WoodenPlanks</defName>
        <label>wooden planks</label>
        <description>Refined wooden planks cut from raw wood. These smooth, uniform boards are perfect for construction and provide better insulation and appearance than raw wood.</description>
        <graphicData>
            <texPath>Things/Item/Resource/WoodenPlanks</texPath>
            <graphicClass>Graphic_StackCount</graphicClass>
        </graphicData>
        <soundInteract>Wood_Drop</soundInteract>
        <soundDrop>Wood_Drop</soundDrop>
        <statBases>
            <MaxHitPoints>60</MaxHitPoints>
            <MarketValue>3.2</MarketValue>
            <Mass>0.4</Mass>
            <Flammability>1.3</Flammability>
            <DeteriorationRate>2</DeteriorationRate>
        </statBases>
        <stuffProps>
            <categories>
                <li>Woody</li>
            </categories>
            <appearance>Planks</appearance>
            <color>(120,100,80)</color>
            <soundImpactStuff>BulletImpact_Wood</soundImpactStuff>
            <soundMeleeHitSharp>MeleeHit_Wood</soundMeleeHitSharp>
            <soundMeleeHitBlunt>MeleeHit_Wood</soundMeleeHitBlunt>
            <statOffsets>
                <WorkToBuild>-200</WorkToBuild>
            </statOffsets>
            <statFactors>
                <MaxHitPoints>0.65</MaxHitPoints>
                <Beauty>1.3</Beauty>
                <WorkToBuild>0.7</WorkToBuild>
                <WorkToMake>0.7</WorkToMake>
                <DoorOpenSpeed>1.0</DoorOpenSpeed>
                <BedRestEffectiveness>1.0</BedRestEffectiveness>
                <MeleeWeapon_CooldownMultiplier>1.2</MeleeWeapon_CooldownMultiplier>
            </statFactors>
        </stuffProps>
        <thingCategories>
            <li>ResourcesRaw</li>
        </thingCategories>
        <burnableByRecipe>true</burnableByRecipe>
        <healthAffectsPrice>false</healthAffectsPrice>
        <minRewardCount>10</minRewardCount>
        <allowedArchonexusCount>80</allowedArchonexusCount>
    </ThingDef>
</Defs>
```

## Defs/ThingDefs_Buildings/Buildings_Production.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<Defs>
    <ThingDef ParentName="BuildingBase">
        <defName>CarpentryBench</defName>
        <label>carpentry bench</label>
        <description>A specialized workbench for processing raw wood into refined wooden planks. Features a sturdy work surface, cutting guides, and storage for carpentry tools.</description>
        <thingClass>Building_WorkTable</thingClass>
        <graphicData>
            <texPath>Things/Building/Production/CarpentryBench</texPath>
            <graphicClass>Graphic_Multi</graphicClass>
            <drawSize>(3,1)</drawSize>
            <damageData>
                <cornerTL>Damage/Corner</cornerTL>
                <cornerTR>Damage/Corner</cornerTR>
                <cornerBL>Damage/Corner</cornerBL>
                <cornerBR>Damage/Corner</cornerBR>
            </damageData>
        </graphicData>
        <castEdgeShadows>true</castEdgeShadows>
        <staticSunShadowHeight>0.20</staticSunShadowHeight>
        <costList>
            <WoodLog>75</WoodLog>
            <Steel>50</Steel>
        </costList>
        <altitudeLayer>Building</altitudeLayer>
        <fillPercent>0.5</fillPercent>
        <useHitPoints>True</useHitPoints>
        <statBases>
            <WorkToBuild>3000</WorkToBuild>
            <MaxHitPoints>180</MaxHitPoints>
            <Flammability>1.0</Flammability>
        </statBases>
        <size>(3,1)</size>
        <designationCategory>Production</designationCategory>
        <passability>PassThroughOnly</passability>
        <pathCost>50</pathCost>
        <hasInteractionCell>True</hasInteractionCell>
        <interactionCellOffset>(0,0,-1)</interactionCellOffset>
        <surfaceType>Item</surfaceType>
        <inspectorTabs>
            <li>ITab_Bills</li>
        </inspectorTabs>
        <building>
            <spawnedConceptLearnOpportunity>BillsTab</spawnedConceptLearnOpportunity>
        </building>
        <comps>
            <li Class="CompProperties_AffectedByFacilities">
                <linkableFacilities>
                    <li>ToolCabinet</li>
                </linkableFacilities>
            </li>
        </comps>
        <placeWorkers>
            <li>PlaceWorker_ShowFacilitiesConnections</li>
        </placeWorkers>
        <researchPrerequisites>
            <li>Smithing</li>
        </researchPrerequisites>
    </ThingDef>
</Defs>
```

## Defs/ThingDefs_Buildings/Buildings_Structure.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<Defs>
    <ThingDef ParentName="BuildingBase">
        <defName>PlankWall</defName>
        <label>plank wall</label>
        <description>A wall constructed from refined wooden planks. More attractive and slightly stronger than regular wooden walls, with better insulation properties.</description>
        <thingClass>Building</thingClass>
        <category>Building</category>
        <graphicData>
            <texPath>Things/Building/Linked/PlankWall</texPath>
            <graphicClass>Graphic_Appearances</graphicClass>
            <linkType>CornerFiller</linkType>
            <linkFlags>
                <li>Wall</li>
                <li>Rock</li>
            </linkFlags>
        </graphicData>
        <uiIconPath>Things/Building/Linked/PlankWall_MenuIcon</uiIconPath>
        <statBases>
            <MaxHitPoints>200</MaxHitPoints>
            <WorkToBuild>500</WorkToBuild>
            <Flammability>1.2</Flammability>
            <Beauty>2</Beauty>
        </statBases>
        <costList>
            <WoodenPlanks>3</WoodenPlanks>
        </costList>
        <leaveResourcesWhenKilled>false</leaveResourcesWhenKilled>
        <altitudeLayer>Building</altitudeLayer>
        <passability>Impassable</passability>
        <blockWind>true</blockWind>
        <castEdgeShadows>true</castEdgeShadows>
        <fillPercent>1</fillPercent>
        <coversFloor>true</coversFloor>
        <placingDraggableDimensions>1</placingDraggableDimensions>
        <tickerType>Never</tickerType>
        <rotatable>false</rotatable>
        <selectable>true</selectable>
        <neverMultiSelect>true</neverMultiSelect>
        <terrainAffordanceNeeded>Light</terrainAffordanceNeeded>
        <holdsRoof>true</holdsRoof>
        <designationCategory>Structure</designationCategory>
        <staticSunShadowHeight>1.0</staticSunShadowHeight>
        <blockLight>true</blockLight>
        <building>
            <isInert>true</isInert>
            <isPlaceOverableWall>true</isPlaceOverableWall>
        </building>
        <damageMultipliers>
            <li>
                <damageDef>Bomb</damageDef>
                <multiplier>2</multiplier>
            </li>
            <li>
                <damageDef>Flame</damageDef>
                <multiplier>1.5</multiplier>
            </li>
        </damageMultipliers>
    </ThingDef>
</Defs>
```

## Defs/RecipeDefs/Recipes_Carpentry.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<Defs>
    <RecipeDef>
        <defName>MakeWoodenPlanks</defName>
        <label>make wooden planks</label>
        <description>Process raw wood into refined wooden planks.</description>
        <jobString>Making wooden planks.</jobString>
        <workAmount>800</workAmount>
        <workSpeedStat>GeneralLaborSpeed</workSpeedStat>
        <effectWorking>ConstructWood</effectWorking>
        <soundWorking>Recipe_Machining</soundWorking>
        <allowMixingIngredients>true</allowMixingIngredients>
        <recipeUsers>
            <li>CarpentryBench</li>
        </recipeUsers>
        <ingredients>
            <li>
                <filter>
                    <thingDefs>
                        <li>WoodLog</li>
                    </thingDefs>
                </filter>
                <count>2</count>
            </li>
        </ingredients>
        <products>
            <WoodenPlanks>1</WoodenPlanks>
        </products>
        <fixedIngredientFilter>
            <thingDefs>
                <li>WoodLog</li>
            </thingDefs>
        </fixedIngredientFilter>
        <workSkill>Crafting</workSkill>
        <skillRequirements>
            <Crafting>2</Crafting>
        </skillRequirements>
    </RecipeDef>

    <RecipeDef>
        <defName>MakeWoodenPlanksBulk</defName>
        <label>make wooden planks x4</label>
        <description>Process raw wood into refined wooden planks in bulk.</description>
        <jobString>Making wooden planks in bulk.</jobString>
        <workAmount>2800</workAmount>
        <workSpeedStat>GeneralLaborSpeed</workSpeedStat>
        <effectWorking>ConstructWood</effectWorking>
        <soundWorking>Recipe_Machining</soundWorking>
        <allowMixingIngredients>true</allowMixingIngredients>
        <recipeUsers>
            <li>CarpentryBench</li>
        </recipeUsers>
        <ingredients>
            <li>
                <filter>
                    <thingDefs>
                        <li>WoodLog</li>
                    </thingDefs>
                </filter>
                <count>8</count>
            </li>
        </ingredients>
        <products>
            <WoodenPlanks>4</WoodenPlanks>
        </products>
        <fixedIngredientFilter>
            <thingDefs>
                <li>WoodLog</li>
            </thingDefs>
        </fixedIngredientFilter>
        <workSkill>Crafting</workSkill>
        <skillRequirements>
            <Crafting>4</Crafting>
        </skillRequirements>
    </RecipeDef>
</Defs>
```

## Languages/English/Keyed/Keys.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<LanguageData>
    <CarpentryBench_Label>carpentry bench</CarpentryBench_Label>
    <CarpentryBench_Description>A specialized workbench for processing raw wood into refined wooden planks.</CarpentryBench_Description>
    
    <WoodenPlanks_Label>wooden planks</WoodenPlanks_Label>
    <WoodenPlanks_Description>Refined wooden planks cut from raw wood. Perfect for construction.</WoodenPlanks_Description>
    
    <PlankWall_Label>plank wall</PlankWall_Label>
    <PlankWall_Description>A wall constructed from refined wooden planks. More attractive than regular wooden walls.</PlankWall_Description>
</LanguageData>
```

## Installation Instructions

1. **Create the mod folder structure** in your RimWorld Mods directory
2. **Add required textures**:
   - `Preview.png` (512x512) - Steam Workshop thumbnail
   - `CarpentryBench.png` (64x64) - The carpentry bench texture
   - `PlankWall_Atlas.png` (64x192) - Wall texture atlas for connected walls
   - `WoodenPlanks.png` (64x64) - Item icon for wooden planks

3. **Test the mod locally**
4. **Upload to Steam Workshop**

## Gameplay Features

**Carpentry Bench:**
- Costs: 75 Wood + 50 Steel
- Requires Smithing research
- Can be linked to Tool Cabinet for efficiency bonus

**Wooden Planks:**
- Made from 2 Wood → 1 Plank
- Acts as a stuff category (can be used for other wooden items)
- Slightly higher beauty than regular wood
- Market value of 3.2 (vs wood's 1.9)

**Plank Walls:**
- Costs: 3 Wooden Planks per wall
- 200 HP (vs 165 for wood walls)
- Beauty +2 (more attractive than regular walls)
- Still flammable but provides good structure

## Balancing Notes

- The 2:1 wood-to-plank ratio means you need 6 wood to make 1 wall section
- Plank walls are stronger and prettier but require processing time
- Tool Cabinet synergy encourages proper workshop setup
- Bulk recipe available for efficient mass production

This creates a nice progression: Raw Wood → Wooden Planks → Better Construction!