#필요 라이브러리 불러오기
library(readr)
library(tidytext)
library(dplyr)

raw_data= read_lines(file.path
          ("C:","Users","user0401","Documents","R",
          "KakaoTalk_20220123_1501_12_572_Sister1.txt"))
raw_data <- data.frame(line = 1:length(raw_data),
                        text = raw_data, 
                        stringsAsFactors = FALSE)
tokenData <- raw_data %>%
   unnest_tokens(word, text)

tidyToken <- tokenData %>%
   anti_join(stop_words)

tidyToken <- tidyToken %>%
   count(word, sort = TRUE)
head(tidyToken) #TOP3 출력
library(wordcloud)
wordcloud(words = tidyToken$word, freq = tidyToken$n, min.freq = 2, max.words = 200, 
          random.order = FALSE, rot.per = 0.35,
          colors = brewer.pal(8, "Dark2"))


