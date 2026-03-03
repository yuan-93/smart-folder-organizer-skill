# Document Classification Rules

## PDF Metadata Extraction & Semantic Classification

When analyzing PDF text, **do not rely purely on rigid keyword matching**. Instead, use your semantic understanding of the document's content to determine its fundamental purpose. Use the guidelines below to categorize the document and extract details for renaming.

If a document matches characteristics of multiple categories, consider its primary purpose. For example, a receipt that mentions a "due date" is still a receipt, and a resume referencing "Internet technologies" is a general Document, not an internet bill.

### Invoices

- **Characteristics**: Documents requesting payment for goods/services provided. Usually contains "Bill To", an Invoice Number, and a Due Date.
- **Naming Format**: `yyyy-mm-dd-[BilledTo]-[VendorName]-[Invoice#]-[Amount].pdf`
- **Folder**: `Documents/Invoices/`

### Bills (Utility/Recurring)

- **Characteristics**: Recurring statements for services like electricity, water, internet, or phone. Contains service periods and account numbers.
- **Naming Format**: `yyyy-mm-dd-[Provider]-[AccountName]-[Account#].pdf`
- **Folder**: `Documents/Bills/`

### Receipts

- **Characteristics**: Proof of payment for a completed transaction. Usually contains an order summary, total paid, and payment method (e.g., "Card Ending In").
- **Naming Format**: `yyyy-mm-dd-[PaidBy]-[Store]-[TotalAmount].pdf`
- **Folder**: `Documents/Receipts/`

### Travel Documents

- **Characteristics**: Itineraries, flight bookings, boarding passes, hotel reservations.
- **Naming Format**: `yyyy-mm-dd-[Airline/Hotel]-[Confirmation#].pdf` (if applicable)
- **Folder**: `Documents/Travel/`

### Financial/Legal

- **Bank Statements**: Monthly account summaries showing available balances and transactions.
- **Legal**: Agreements, contracts, privacy policies.
- **Folder**: `Documents/Financial/` or `Documents/Legal/`

### Career & Professional

- **Characteristics**: Resumes, Job applications, CVs, and professional summaries.
- **Folder**: `Documents/Career/`

### General Documents

- **Characteristics**: General documents that do not fall into the above categories.
- **Folder**: `Documents/`

## General File Types

### Photos & Media

- **Photos**: `.jpg`, `.jpeg`, `.png`, `.heic`, `.webp`. Move to `Photos/`.
- **Screenshots**: Filenames containing "Screenshot" (Windows/iOS) or "Screen Shot" (macOS). Move to `Photos/Screenshots/`.
- **Videos**: `.mp4`, `.mov`, `.mkv`, `.avi`. Move to `Videos/`.

### Installers

- **Extensions**: `.dmg`, `.pkg`, `.exe`, `.msi`, `.app` (if in a folder).
- **Folder**: `Installers/`

### Archives

- **Extensions**: `.zip`, `.tar.gz`, `.rar`, `.7z`.
- **Folder**: `Archives/`
