<template>

<header v-if="article" class="article_header">
	<div class="article_header_info">
		<span>{{formattedDate}}</span>
		<h1>{{article.title}}</h1>
	</div>
	<img :src="article.imgURL" alt="article image">
</header>

<div class="main">
	<main class="articlePage">
		<article v-if="article" class="article">
			<p>{{article.content.slice(0, 670)}}</p>
			<img :src="article.imgURL" alt="article image">
			<p>{{article.content.slice(670)}}</p>

			<img src="../assets/socialMediaPlaceholder.png" alt="social media placeholder">
		</article>

		<Banner />

		<section v-if="author" class="author">
			<h2>About the author</h2>
			
			<div class="author_info">
				<div class="author_info_imgWrapper">
					<img :src="author.imgURL" :alt="author.name">	
				</div>
				<div class="author_info_aboutMe">
					<p>{{author.AboutMe}}</p>
				</div>
			</div>
		</section>

		<section class="comments">
			<h2>Comments</h2>

			<div v-if="comments" class="comments_commentList">
				<Comment :key="comment.id" :comment="comment" v-for="comment in comments"/>
			</div>
			<div v-else class="comments_noComments">
				<span>No comments</span>
			</div>

			<form class="comments_addComment" @submit.prevent="addNewComment()">
				<h3>Add Your Comment</h3>
				<input type="text" placeholder="Name" v-model="newComment.user" required>
				<input type="email" placeholder="Email Address" v-model="newComment.email" required>
				<textarea placeholder="Comment" v-model="newComment.text" required></textarea>
				<button type="submit">Submit</button>
			</form>
		</section>
	</main>

	<Sidebar />
</div>

</template>

<script>
import dayjs from "dayjs";

import Banner from "@/components/banner.vue";
import Comment from "@/components/comment.vue";
import Sidebar from "@/components/sidebar/sidebar.vue";

export default {
	name: "Article",
	components: { Banner, Comment, Sidebar },
	data(){
		return{
			article: null,
			author: null,
			comments: null,

			newComment: {}
		}
	},
	computed:{
		articleId(){
			return this.$route.params.articleId;
		},
        formattedDate(){
            const date = this.article.date * 1000;
            return dayjs(date).format('MMMM DD, YYYY');
        },
	},
	methods:{
		// add meta info about new comment, append it to the comment list and clear the inputted values
		addNewComment(){
			this.newComment.id = Date.now();
			this.newComment.date = Date.now() / 1000;

			if(!this.comments) this.comments = [];
			this.comments.push(this.newComment);

			this.newComment = {};
		},
		setArticleContent(){
			this.$store.dispatch("fetchArticleList");
			this.$store.dispatch("fetchAuthorList");
			this.$store.dispatch("fetchCommentList");

			this.article = this.$store.getters.getArticleById(this.articleId);
			this.author = this.$store.getters.getAuthorById(this.article.authorId);
			this.comments = this.$store.getters.getCommentsOfArticle(this.article.commentIds);
		}
	},
	mounted(){
		this.setArticleContent();
	},
	watch:{
		// if article changes set its content again
		articleId(){
			if(!this.articleId) return;
			this.setArticleContent();
		}
	}
}
</script>

<style lang="scss" scoped>
@import "@/styles/main.scss";

.article_header{
	max-width: 100%;

	margin-bottom: 8px;

	position: relative;

	& > img{
		max-width: 100%;
	}

	& > .article_header_info {
		width: 100%;
		min-height: 50px;

		padding: 32px;

		position: absolute;
		bottom: 0;

		background: rgb(238,238,238);
		background: linear-gradient(0deg, rgba(238,238,238,1) 15%, rgba(0,0,0,0) 100%);

		& > h1{
			@include fontStyle($bitter, 44px, bold, 55px, #222222);
		}
		& > span{
			@include fontStyle($varelaRound, 12px, normal, 14px, #222222);
		}
	}
}

.main{
	display: flex;
	justify-content: space-between;

	& > .articlePage{
		max-width: 620px;
	}
}

.article{
	background-color: white;

	& img{
		max-width: 100%;

		&:last-of-type{
			margin-bottom: 20px;
		}
	}

	& > p{
		@include fontStyle($bitter, 14px, normal, 22px, #444444);
		padding: 36px 20px 40px 30px;
	}
}

.author{
	width: 100%;

	padding: 18px 26px 40px 32px;
	margin-bottom: 16px;

	background-color: white;

	h2{
		@include fontStyle($bitter, 24px, bold, 28px, #363F48);
	}

	.author_info{
		display: flex;
		gap: 20px;

		margin-top: 28px;

		& img{
			max-width: 110px;
			aspect-ratio: 1/1;
		}

		p{
			@include fontStyle($varelaRound, 13px, normal, 22px, #444444);
		}
	}
}

.comments{
	padding: 16px 28px 28px 32px;
	margin-bottom: 44px;

	background-color: white;

	& h2, h3{
		@include fontStyle($bitter, 24px, bold, 28px, #363F48);
	}

	& > .comments_commentList{
		margin-top: 44px;
		margin-bottom: 32px;
	}

	& > .comments_noComments{
		min-height: 120px;

		display: flex;
		align-items: center;
		justify-content: center;

		margin-top: 44px;
		margin-bottom: 32px;

		border: 1px solid black;
	}

	& > .comments_addComment{
		display: flex;
		flex-direction: column;

		& > h3{
			margin-bottom: 16px;
		}

		& > input{
			@include fontStyle($varelaRound, 14px, normal, 14px, #666666);

			width: 300px;

			padding: 12px 0px 16px 20px;
			margin-bottom: 8px;

			border: none;
			background-color: #DDDDDD;
		}

		& > textArea{
			@include fontStyle($varelaRound, 14px, normal, 14px, #666666);

			min-width: 100%;
			min-height: 180px;

			padding: 12px 0px 16px 20px;

			resize: none;

			border: none;
			background-color: #DDDDDD;
		}

		& > button{
			@include fontStyle($varelaRound, 14px, normal, 16px, #FFFFFF);

			width: fit-content;
			min-width: 150px;

			padding: 16px 36px;
			margin-top: 32px;

			text-align: center;

			border: none;
			background-color: $primary;
		}
	}
}
</style>