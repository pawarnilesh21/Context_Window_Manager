function App() {
  return (
    <div className="min-h-screen bg-slate-950 flex items-center justify-center px-6">
      <div className="text-center">
        <div className="w-20 h-20 mx-auto mb-6 rounded-2xl bg-indigo-600/20 border border-indigo-500/30 flex items-center justify-center">
          <span className="text-4xl text-indigo-400">⌘</span>
        </div>

        <h1 className="text-4xl md:text-6xl font-bold text-white tracking-tight">
          Context Window Manager
        </h1>

        <p className="mt-5 text-lg text-slate-400 max-w-xl mx-auto leading-relaxed">
          Understand how tokens, tokenization, and context windows work. Explore
          context limits and learn how context overflow happens in Large
          Language Models.
        </p>

        <div className="mt-8 flex flex-wrap justify-center gap-3">
          <span className="px-4 py-2 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-300 text-sm">
            Tokens
          </span>

          <span className="px-4 py-2 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-300 text-sm">
            Tokenization
          </span>

          <span className="px-4 py-2 rounded-full bg-purple-500/10 border border-purple-500/20 text-purple-300 text-sm">
            Context Window
          </span>

          <span className="px-4 py-2 rounded-full bg-red-500/10 border border-red-500/20 text-red-300 text-sm">
            Context Overflow
          </span>
        </div>

        <p className="mt-12 text-sm text-slate-600">
          A Learning Project for Understanding LLM Context Management
        </p>
      </div>
    </div>
  );
}

export default App;
