## 例子

### 生成菜单

```bash
python -m recipe_reduce.menu --lang zh
```

### 在 `input.json` 中填入份数

```json
{
  "count": {
    "甜粘三文鱼 配 烤蔬菜和米饭": 2,
    "柠檬刺山柑猪排和帕尔马玉米粥 配 迷迭香和大蒜烤青豆": 2
  },
  "info": {}
}
```

### 获取购买清单

```bash
python -m recipe_reduce.main --lang zh
```

| Name         |   Quantity | Unit   | Link                    |
|--------------|------------|--------|-------------------------|
| 三文鱼       |      10.00 | oz     | https://amzn.to/3yWqPLE |
| 猪排         |      12.00 | oz     | https://amzn.to/3stpR8x |
| 豆角         |       1.00 | lb     | https://amzn.to/3mxVtG9 |
| 甜椒         |       1.00 | pc.    | https://amzn.to/3mvDK20 |
| 香米         |       5.00 | oz     | https://amzn.to/3erED7e |
| 意式玉米粥   |       3.00 | oz     | https://amzn.to/3qoqehV |
| 帕尔马干酪   |       0.75 | oz     | https://amzn.to/3syP9C6 |
| 日本酱油     |       0.50 | oz     | https://amzn.to/3Hdp6oi |
| 泰式甜辣酱   |       3.00 | oz     | https://amzn.to/3Frkn1N |
| 火鸡汤浓缩液 |       1.00 | pkt    |                         |
| 细香葱       |       0.25 | oz     | https://amzn.to/30UCi1A |
| 迷迭香       |       0.25 | oz     | https://amzn.to/3quz6To |
| 大蒜         |       2.00 | pc.    | https://amzn.to/3H8ENNb |
| 芝麻         |       0.25 | oz     | https://amzn.to/3JiZbgL |
| 酸橙         |       1.00 | oz     | https://amzn.to/3mtUwhW |
| 柠檬         |       1.00 | pc.    | https://amzn.to/3yYFlmg |
| 刺山柑       |       1.00 | oz     | https://amzn.to/3syQ5X8 |
