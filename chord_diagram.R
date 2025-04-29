library(circlize)
library(dplyr)
library(readxl)
library(tidyr)
library(RColorBrewer)

# 读取 Enrichment 表格
go_data <- read_excel("metascape_result.t57qvuh3c.xlsx", sheet = "Enrichment")

# 选出前 10 个 LogP 最小（显著性最高）的条目
top10 <- go_data %>%
  arrange(LogP) %>%
  slice(1:10)
# 拆分 Genes 字符串为单独的基因
df <- top10 %>%
  select(Term, Genes) %>%
  mutate(Genes = strsplit(Genes, ",\\s*")) %>%
  unnest(Genes)

# 查看数据格式
head(df)
# 设置颜色
terms <- unique(df$Term)
genes <- unique(df$Genes)
all_labels <- c(terms, genes)

grid.col <- setNames(
  c(colorRampPalette(brewer.pal(8, "Set3"))(length(terms)),
    rep("lightgrey", length(genes))),
  all_labels
)

# 开始画图
chordDiagram(df, grid.col = grid.col, transparency = 0.2)

# 添加标题
title("Top 10 GO Terms Enriched - Chord Diagram (Metascape)", cex.main = 1.2)