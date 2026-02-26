# Dict-CLI

A simple command-line dictionary tool using Youdao Dictionary API.

## Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/Dict-CLI.git
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
n. 苹果

E.g.
1. She crunched her apple noisily.
2. Someone threw an apple core.
3. Sling me an apple, will you?
```

## Features

- Fetch word definitions from Youdao Dictionary
- Display 3 example sentences
- No external dependencies (pure Python)

## Requirements

- Python 3.8+

## License

MIT
