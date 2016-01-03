newsPre = open('news-pre.txt', 'r')
newsContent = open('news-raw.txt', 'r')
newsPost = open('news-post.txt', 'r')

outfile = open('Active/news.html', 'w')
outfile.writelines(newsPre.readlines() + newsContent.readlines() + newsPost.readlines())
