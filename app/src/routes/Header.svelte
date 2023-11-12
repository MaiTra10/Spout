<script>
	import { page } from '$app/stores';
	import logo from '$lib/images/spout.png';
</script>

<header class="flex justify-between items-center h-24 sticky w-10/12">
	<div class="flex w-60 justify-center items-center">
		<a href="/">
			<img src={logo} alt="Spout" />
		</a>
	</div>

	<nav class="flex items-center justify-center md:order-none text-xl flex-1 ">
		<ul>
			<li aria-current={$page.url.pathname === '/' ? 'page' : undefined}>
				<a href="/">My Home</a>
			</li>
			<li aria-current={$page.url.pathname === '/about' ? 'page' : undefined}>
				<a href="/about">About</a>
			</li>
			<li aria-current={$page.url.pathname === '/Support' ? 'page' : undefined}>
				<a href="/Support">Support</a>
			</li>
		</ul>
	</nav>
	<div class="w-72 flex justify-end items-center ">
		<a href="" class="bg-primary h-12 w-36 rounded-md flex justify-center items-center text-white">
			Login
		</a>
	</div>

</header>


<style>


	ul {
		position: relative;
		padding: 0;
		margin: 0;
		height: 3em;
		width: 15em;
		display: flex;
		justify-content: space-between;
		align-items: center;
		list-style: none;
		background: var(--background);
		background-size: contain;
	}

	li {
		position: relative;
		height: 100%;
	}

	li[aria-current='page']::before {
		--size: 6px;
		content: '';
		width: 0;
		height: 0;
		position: absolute;
		top: 0;
		left: calc(50% - var(--size));
		border: var(--size) solid transparent;
		border-top: var(--size) solid var(--color-theme-1);
	}

	nav a {
		display: flex;
		height: 100%;
		align-items: center;
		padding: 0 0.5rem;
		color: var(--color-text);
		font-weight: 700;
		font-size: 0.8rem;
		text-transform: uppercase;
		letter-spacing: 0.1em;
		text-decoration: none;
		transition: color 0.2s linear;
	}

</style>
