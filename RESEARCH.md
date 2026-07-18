# Data/ML expansion: research and provenance

Дата аудита: 2026-07-18.

## Что было до расширения

В Codex-библиотеке было 58 скиллов и 6 агентов. `mle-workflow` покрывал общий production ML lifecycle, а Jupyter и spreadsheet-инструменты давали способы работать с файлами. Не было отдельных процессов и ролей для data analysis, SQL, analytics engineering, data engineering, data architecture, BI, data governance и causal inference. В старом `mle-workflow` также были ссылки на отсутствующие пакеты, а `strategic-compact` зависел от Claude-hook и несуществующего локального скрипта.

## Claude-репозиторий пользователя

Проверен [pavelMMF/claude-agents-and-skills](https://github.com/pavelMMF/claude-agents-and-skills) на коммите `7d6c11bdf0e78900215c4684383f2f70ddd26af7`: 353 `SKILL.md`, 14 верхнеуровневых агентов, один массовый коммит, без корневых README и LICENSE.

Репозиторий использован как инвентарь, но не как источник для прямого копирования. Отсутствие общей лицензии и provenance не позволяет безопасно перепубликовать зеркало целиком.

Data/ML-профили в нём байт-в-байт совпадают с MIT-источником [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) на `947b44ca0c58d606b084e9cb1a2389335b49278b`. Они не перенесены дословно: исходные Claude-модели, широкие Write/Edit/Bash-права, несуществующий context-manager protocol, демонстрационные бизнес-результаты и абсолютные обещания удалены. Новые TOML-профили написаны заново, сокращены и закреплены в read-only режиме.

## Добавленные источники

| Источник | Версия | Лицензия | Использование | Вердикт |
|---|---|---|---|---|
| [dbt-labs/dbt-agent-skills](https://github.com/dbt-labs/dbt-agent-skills) | `f8d7828e5cb51016143d0a4e2b5116ca711a44c6` | Apache-2.0 | Четыре dbt-скилла с локальными LICENSE и Codex safety-адаптацией | allow with edits |
| [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | `947b44ca0c58d606b084e9cb1a2389335b49278b` | MIT | Ролевая карта для новых компактных TOML-агентов; текст написан заново | inspiration only |
| [Agent Skills for Context Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | `c578e85e40fe2bda7c1fec91ff64cf5285434934` | MIT | Идеи для `context-budget`; без копирования скриптов | allow with edits |
| [Everything Claude Code](https://github.com/affaan-m/ECC) | `754b8dd76ca885b764ec22f476664377aa46b6cd` | MIT | Сравнение context/token workflows; переписано под Codex | allow with edits |
| [causal-inference-skill](https://github.com/ruoyanhuang216/causal-inference-skill) | `05c57` | MIT | Проверка охвата causal workflow; без копирования кода | allow with edits |

У dbt-пакетов есть собственные `PROVENANCE.md` и `LICENSE.txt`.

## Что сознательно не импортировано

- Всё Claude-зеркало целиком: неясная репозиторная лицензия и сильное дублирование.
- `token-budget-advisor`: перекрывается с существующим `token_budgeter` и добавляет лишний вопрос почти к каждому запросу; полезные идеи объединены в `context-budget`.
- `cost-tracking`: жёстко зависит от Claude-specific `~/.claude/metrics/costs.jsonl`, которого у Codex нет как подтверждённого источника.
- `embeddings`: предлагает запуск неаудированного `npx claude-flow`.
- Семь длинных context-engineering скиллов: большая часть уже покрыта `context-rot-defense`, `checkpoint`, `planning-with-files`, `strategic-compact` и `memory-keeper`.
- dbt MCP configuration и troubleshooting automation: не нужны для базового набора и имеют более широкую сетевую и операционную поверхность.

## Итоговая архитектура

Добавлены десять собственных Codex-скиллов, четыре лицензированных dbt-скилла и шесть read-only агентов. `strategic-compact` переписан без Claude-зависимостей, а `mle-workflow` заменён на связный маршрут, который ссылается только на реально присутствующие компоненты.

Точные файлы и описания находятся в [CATALOG.md](CATALOG.md) и [catalog.json](catalog.json).

## Creator и game/3D expansion

Дата аудита: 2026-07-18. Перед расширением в библиотеке уже были общие `content-engine`, `brand`, `brand-voice` и специализированные RTS-пайплайны. Не хватало отдельных процессов для проверки creator-аудитории и оффера, безопасных AI-персон, измеряемого роста и монетизации, а также общего цикла game design → engine → 3D assets → animation → profiling → playtest.

| Источник | Проверенная версия | Лицензия | Использование | Вердикт |
|---|---|---|---|---|
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | `67264763cb107d61749f418d081c56e5bcbc0209` | MIT | Карта задач customer research, offers, video, launch, email и growth loops; инструкции написаны заново под Codex | allow with edits |
| [fagemx/gstack-game](https://github.com/fagemx/gstack-game) | `7259ab9782fa9c17e45c16f1fb8347823ddb4379` | MIT | Идеи для vertical slice, feel pass, asset review, playtest, QA и engineering review; реализация не копировалась | inspiration only |
| [alexmeckes/godot-claude-skills](https://github.com/alexmeckes/godot-claude-skills) | `881ff9d285b8dfa5e343ce1b32bdcff367fe89f8` | MIT | Проверка охвата Godot scenes, scripts и shaders; маршруты переписаны и привязаны к официальной документации | inspiration only |
| [akiojin/skills](https://github.com/akiojin/skills) | `4f72afeb9efb9520a7a02afb9e23fba2dbe0ffa1` | MIT | Проверка заявленного Unity-покрытия; подходящего Unity-пакета в зафиксированном дереве не найдено | reject unavailable material |

Для фактических ограничений использованы первичные источники: документация Unity, Unreal Engine, Godot, Blender и Khronos glTF, а для синтетического контента — правила YouTube о disclosure, impersonation и monetization. Ссылки находятся в `references/sources.md` соответствующих скиллов.

### Что сознательно не импортировано

- `.claude`-пути, shell-предисловия, hooks, локальная телеметрия и repo-specific binaries из Claude-наборов;
- команды установки и запуска непроверенных npm-пакетов, а также запросы API-ключей без необходимости;
- статические обещания результата, фальшивые отзывы, доходы или дефицит, массовый неаутентичный контент и нераскрытая имитация личности;
- неподтверждённые Unity-материалы, которых не оказалось в зафиксированной версии источника.

Добавлены семь creator-скиллов и девять game/3D-скиллов. Все они созданы в стандартной структуре Codex (`SKILL.md`, `agents/openai.yaml`, `references/`) и используют внешние репозитории только как исследовательский материал, а не как исполняемую зависимость.
