# Dict-CLI

A simple command-line dictionary tool using Youdao Dictionary API.

## Installation

```bash
# Clone the repository
git clone https://github.com/Tenaryo/Dict-CLI.git
cd Dict-CLI

# Install to your PATH
cp dict_cli/main.py ~/.local/bin/dict
chmod +x ~/.local/bin/dict
```

Make sure `~/.local/bin` is in your `$PATH`.

## Usage

```bash
dict <word>
```

### Example

```bash
$ dict apple
```

Output:
```
apple
────────────────────────────────────────
  n. 苹果

例句:
  1. She crunched her apple noisily.
     她吃苹果发出嘎嚓嘎嚓的声音。
  2. Someone threw an apple core.
     有人扔了一个苹果核。
  3. Sling me an apple, will you?
     扔个苹果给我，好吗？
```

### Multi-part-of-speech Example

```bash
$ dict run
```

Output:
```
run
────────────────────────────────────────
  v. 跑，奔跑；参加（赛跑），举行（比赛）...
  n. 跑步，赛跑；旅程，航程；一系列（成功或失败）...

例句:
  1. I can't run any faster.
     我不能跑得更快了。
  2. Engines won't run without lubricants.
     没有润滑油发动机就不能运转。
  3. 'Run!' he shouted.
     "跑！"他大喊一声。
```

## Features

- Fetch word definitions from Youdao Dictionary
- Display translations grouped by part of speech (n., v., adj., etc.)
- Display 3 example sentences with Chinese translations
- Colorful output for better readability
- No external dependencies (pure Python)

## Requirements

- Python 3.8+

## License

MIT
