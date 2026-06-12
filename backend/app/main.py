app = FastAPI(
    title="PayGuard DQ API",
    middleware=[
        CORSMiddleware(
            allow_origins=["http://localhost:3000"],
            allow_credentials=True,
            allow_methods="*",
            allow_headers="*"
        )
    ]
)
    description="GenAI Agent for Universal, Dimension-Based Data Quality Scoring in Payments",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(ingest.router)
app.include_router(runs.router)


@app.get("/")
async def root():
    """Health check endpoint."""
    return {
        "service": "Data Quality Scoring API",
        "status": "healthy",
        "version": "1.0.0"
    }


@app.get("/health")
async def health():
    """Health check."""
    return {"status": "ok"}
