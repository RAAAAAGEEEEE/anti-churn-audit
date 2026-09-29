# Installation

Voir aussi : [USAGE.md](USAGE.md), [CONFIGURATION.md](CONFIGURATION.md),
[TROUBLESHOOTING.md](TROUBLESHOOTING.md).

## Prérequis

- Claude Code, dans une version qui charge les skills depuis
  `.claude/skills/`.
- Python 3.8 ou plus, bibliothèque standard uniquement, pour les deux
  validateurs de `scripts/`. L'audit lui-même n'a pas besoin de Python.
- Un checkout local du dépôt à auditer.

## Installation personnelle (tous vos projets)

```bash
git clone https://github.com/RAAAAAGEEEEE/anti-churn-audit ~/.claude/skills/anti-churn-audit
```

Sous Windows PowerShell :

```powershell
git clone https://github.com/RAAAAAGEEEEE/anti-churn-audit "$env:USERPROFILE\.claude\skills\anti-churn-audit"
```

## Installation par projet

Depuis la racine du dépôt à auditer :

```bash
mkdir -p .claude/skills
git clone https://github.com/RAAAAAGEEEEE/anti-churn-audit .claude/skills/anti-churn-audit
```

Ajoutez `.claude/skills/anti-churn-audit/` au `.gitignore` de ce dépôt si vous
ne voulez pas versionner le skill.

## Vérifier l'installation

Lancer `/anti-churn-audit audit` dans une session Claude Code, puis vérifier
que les validateurs tournent :

```bash
python3 ~/.claude/skills/anti-churn-audit/scripts/validate_report.py ~/.claude/skills/anti-churn-audit/examples/stripe-incomplete/anti-churn-audit.json
```

Sortie attendue : une ligne commençant par `[OK]`.

## Mettre à jour

```bash
git -C ~/.claude/skills/anti-churn-audit pull
```
