# Codex agents & skills

Личная библиотека профилей агентов и скиллов для Codex. Это переносимый снимок рабочей конфигурации: скиллы описывают повторяемые процессы и подключают нужные материалы или скрипты, а агенты задают узкие роли для независимой проверки и делегирования.

Сейчас в репозитории:

- **91 скилл** — включая отдельные стеки для аналитики и ML, оптимизации баз данных, blockchain-разработки, creator-бизнеса, геймдева и 3D-производства;
- **12 агентов** — в том числе `data_analyst`, `analytics_engineer`, `data_engineer`, `data_architect`, `ml_architect` и `experiment_reviewer`;
- полный [каталог](CATALOG.md) и его [машиночитаемая версия](catalog.json).

## Как это устроено

```text
.
├── agents/             # TOML-профили специализированных агентов
├── skills/             # Один каталог на скилл; точка входа — SKILL.md
├── scripts/            # Сборка каталога и проверки репозитория
├── CATALOG.md          # Список агентов и скиллов для чтения
└── catalog.json        # Те же метаданные для инструментов
```

Скилл — это папка с обязательным `SKILL.md`. В нём находятся метаданные и инструкции, по которым Codex понимает, когда и как применять скилл. Рядом могут лежать `scripts/`, `references/`, `assets/`, шаблоны и файлы лицензий.

Профиль агента — TOML-файл с ролью, уровнем рассуждения, режимом песочницы и отдельными developer instructions. Такие профили полезны, когда задачу стоит разложить на независимые точки зрения: например, отдельно проверить архитектуру, продуктовый смысл и UI/UX.

## Основные группы скиллов

- **Оркестрация и контекст:** `agentic-startup-orchestrator`, `planning-with-files`, `checkpoint`, `context-rot-defense`, `parallel-delegation-protocol`.
- **Разработка и архитектура:** `codebase-design`, `coding-standards`, `backend-patterns`, `frontend-patterns`, `api-design`, `tdd`, `diagnosing-bugs`.
- **Документация и контент:** `anti-slop-writing`, `article-writing`, `brand-voice`, `content-engine`, `documentation-lookup`.
- **UI/UX и дизайн:** `ui-ux-pro-max`, `ui-styling`, `design-system`, `better-icons`, набор скиллов для Figma.
- **Исследование и оценка:** `deep-research`, `autoresearch`, `benchmark-methodology`, `eval-harness`, `verification-loop`.
- **Инструменты и интеграции:** `cli-creator`, `mcp-server-patterns`, `playwright`, `gh-address-comments`, `gh-fix-ci`.
- **Безопасность:** review, threat modeling, ownership map и практики для Python, JavaScript/TypeScript и Go.
- **Data analytics и BI:** `data-analysis`, `sql-databases`, `bi-data-visualization`, `experimentation-causal-inference`.
- **Database performance:** `sql-databases` с отдельными playbook’ами для execution plans, индексов, статистики, блокировок, online schema changes и backfill.
- **Blockchain:** `blockchain-development`, `solidity-smart-contracts`, `smart-contract-security` — от wallet/RPC/indexer-архитектуры до контрактов, fuzz/invariant tests и аудита.
- **Analytics engineering и dbt:** `analytics-engineering`, `using-dbt-for-analytics-engineering`, `adding-dbt-unit-test`, `building-dbt-semantic-layer`, `working-with-dbt-mesh`.
- **Data platform:** `data-engineering`, `data-architecture`, `data-quality-governance`.
- **ML-системы:** `mle-workflow` и `ml-system-architecture` — от data contracts и baseline до serving, monitoring и rollback.
- **Creator и дистрибуция:** `creator-audience-research`, `creator-positioning-offers`, `short-form-video`, `ai-persona-studio`, `creator-growth-experiments`, `creator-monetization`, `creator-email-launch`.
- **Game development и 3D:** `game-design`, `gameplay-systems`, `level-design`, `game-engine-development`, `blender-game-assets`, `technical-art`, `game-animation`, `game-performance`, `game-playtest-qa`, а также специализированные RTS-пайплайны.

## Database и blockchain-набор

Для баз данных не создан второй дублирующий router: существующий `sql-databases` усилен отдельными reference-playbook’ами. Performance-процесс идёт от workload evidence и execution plan к одной проверяемой гипотезе, а schema changes используют expand/migrate/contract, bounded backfill, lock/lag guards и реальный план отката.

Blockchain-набор разделён по ответственности. `blockchain-development` покрывает сеть, RPC, кошельки, транзакции, подтверждения, reorg и индексаторы; `solidity-smart-contracts` — EVM-контракты и тестирование; `smart-contract-security` — entry points, invariants, роли, экономические атаки и доказательные findings. Seed phrases, private keys, mainnet-транзакции и deployment без явного разрешения запрещены.

## Creator и game/3D-набор

Creator-набор покрывает путь от проверки аудитории и позиционирования до производства коротких видео, роста, email-запуска и выбора монетизации. `ai-persona-studio` предназначен для оригинальных или лицензированных AI-персон: он требует согласия на использование внешности и голоса, прозрачного раскрытия синтетического контента и редакторской проверки. Фальшивые отзывы, доходы, дефицит и массовый неаутентичный контент исключены из процесса.

Game/3D-набор разделяет решения по уровню ответственности: дизайн опыта, игровые системы, уровни, реализация в Unity/Unreal/Godot, Blender-пайплайн, technical art, анимация, производительность и playtest/QA. Он не подменяет запуск редактора или профайлера: непроверенные результаты маркируются как гипотезы, а реальные бюджеты и ограничения берутся из проекта.

## Data/ML-набор

Новые скиллы разделены по типу решения: анализ отвечает на вопрос по данным, analytics engineering создаёт доверенный слой моделей и метрик, data engineering строит надёжное движение данных, data architecture определяет границы и контракты платформы, а ML architecture проектирует полный жизненный цикл модели. Это уменьшает конфликт триггеров и не заставляет загружать один гигантский универсальный prompt.

Все шесть новых агентов работают в `read-only` sandbox. Они предназначены для независимого анализа и ревью; production-запуски, миграции, backfill, изменение трафика и прав доступа требуют отдельного явного разрешения.

Отчёт об источниках, лицензиях, исключённых материалах и сравнении с Claude-репозиторием находится в [RESEARCH.md](RESEARCH.md).

Точное назначение каждого пакета приведено в [CATALOG.md](CATALOG.md).

## Установка

Нужен Codex с поддержкой skills и custom agents. По умолчанию личная конфигурация находится в `$CODEX_HOME`; если переменная не задана, обычно используется каталог `.codex` в домашней папке.

PowerShell:

```powershell
$targetCodexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path ([Environment]::GetFolderPath('UserProfile')) '.codex' }
New-Item -ItemType Directory -Force -Path "$targetCodexHome\skills", "$targetCodexHome\agents" | Out-Null
Copy-Item .\skills\* "$targetCodexHome\skills" -Recurse -Force
Copy-Item .\agents\*.toml "$targetCodexHome\agents" -Force
```

После копирования перезапустите Codex, чтобы он заново обнаружил скиллы и агентов. Не обязательно устанавливать всё: можно скопировать только нужные папки из `skills/` и отдельные TOML-файлы из `agents/`.

## Зависимости и переносимость

Репозиторий хранит конфигурацию и вспомогательные ресурсы, но не устанавливает внешние зависимости автоматически. Отдельным скиллам могут понадобиться Python, Node.js, `gh`, Playwright, MCP-серверы, плагины или доступ к браузеру. Проверяйте `SKILL.md` выбранного пакета перед использованием.

Локальные абсолютные пути в этом снимке заменены на `$CODEX_HOME`. Секреты, системные скиллы Codex, plugin-cache, логи, память, checkpoints и пользовательские credential/config-файлы в репозиторий не включены.

## Обновление каталога

После добавления или изменения пакетов выполните:

```powershell
powershell -NoProfile -File .\scripts\build-catalog.ps1
powershell -NoProfile -File .\scripts\validate-repo.ps1
```

## Лицензии и происхождение

Это снимок личной рабочей библиотеки, в которой есть как авторские, так и адаптированные пакеты. Если внутри папки скилла есть `LICENSE`, `LICENSE.txt`, `NOTICE` или `NOTICE.txt`, эти условия относятся к содержимому соответствующей папки. Отсутствие файла лицензии не означает автоматического разрешения на копирование или распространение. Общая лицензия намеренно не назначена всему репозиторию. Подробный provenance приведён в [RESEARCH.md](RESEARCH.md) и локальных `PROVENANCE.md`.
